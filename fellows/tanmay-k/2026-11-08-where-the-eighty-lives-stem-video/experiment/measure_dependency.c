// Same weights, same MACs; only the dependency differs.
#include <string.h>
// A: recurrent  -> T steps, each a matvec that needs the previous step's output.
// B: parallel   -> the same weight matrix applied to T independent rows (one matmul), as a conv applies one filter at every position.
// Single thread, float32, batch 1. Build: clang -O3 -o measure_dependency measure_dependency.c -framework Accelerate
#include <Accelerate/Accelerate.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
static double now(){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec*1e3+t.tv_nsec/1e6;}
static float sg(float z){return 1.f/(1.f+expf(-z));}
int cmp(const void*a,const void*b){double x=*(double*)a,y=*(double*)b;return (x>y)-(x<y);}
int main(int argc,char**argv){
  int h=128,x=262,K=h+x,N=4*h;                 // 0.2M params
  float*W=malloc(sizeof(float)*K*N),*in=malloc(sizeof(float)*K),*z=malloc(sizeof(float)*N);
  for(int i=0;i<K*N;i++)W[i]=((i*2654435761u)%1000)/1e5f; for(int i=0;i<K;i++)in[i]=0.01f*(i%7);
  int Ts[]={10,25,50,100,200,400}; int REP=41;
  printf("params=%d  MACs/step=%d\nT,MACs(M),recurrent_ms,parallel_ms,ratio\n",K*N,K*N);
  for(int ti=0;ti<6;ti++){int T=Ts[ti];
    float*X=malloc(sizeof(float)*T*K),*Y=malloc(sizeof(float)*T*N),*c=calloc(h,4),*hh=calloc(h,4);
    for(int i=0;i<T*K;i++)X[i]=0.01f*(i%11);
    double ra[41],rb[41];
    for(int r=0;r<REP;r++){
      memset(c,0,h*4);memset(hh,0,h*4);
      double t0=now();
      for(int t=0;t<T;t++){
        memcpy(in,X+(size_t)t*K,x*4); memcpy(in+x,hh,h*4);
        cblas_sgemv(CblasRowMajor,CblasTrans,K,N,1.f,W,N,in,1,0.f,z,1);
        #ifndef NOELEM
        for(int j=0;j<h;j++){float i_=sg(z[j]),f=sg(z[h+j]),g=tanhf(z[2*h+j]),o=sg(z[3*h+j]);c[j]=f*c[j]+i_*g;hh[j]=o*tanhf(c[j]);}
#else
        for(int j=0;j<h;j++)hh[j]=z[j];
#endif
      }
      ra[r]=now()-t0;
      t0=now();
      cblas_sgemm(CblasRowMajor,CblasNoTrans,CblasNoTrans,T,N,K,1.f,X,K,W,N,0.f,Y,N);
      for(int t=0;t<T;t++)
#ifndef NOELEM
      for(int j=0;j<h;j++){float i_=sg(Y[t*N+j]),f=sg(Y[t*N+h+j]),g=tanhf(Y[t*N+2*h+j]),o=sg(Y[t*N+3*h+j]);float c_=f*0.5f+i_*g;Y[t*N+j]=o*tanhf(c_);}
#endif
       // same-size nonlinearity, no dependency
      rb[r]=now()-t0;
    }
    qsort(ra,REP,8,cmp);qsort(rb,REP,8,cmp);
    printf("%d,%.1f,%.4f,%.4f,%.1f\n",T,(double)T*K*N/1e6,ra[REP/2],rb[REP/2],ra[REP/2]/rb[REP/2]);
  }
}
