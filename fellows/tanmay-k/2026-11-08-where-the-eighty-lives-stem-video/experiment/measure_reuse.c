// Same, but the parallel form reuses each loaded weight across RB positions (weight reuse, plain C, vectorised).
// Build: clang -O3 -fno-vectorize -fno-slp-vectorize -o measure_scalar measure_scalar.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
static double now(){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec*1e3+t.tv_nsec/1e6;}
static float sg(float z){return 1.f/(1.f+expf(-z));}
int cmp(const void*a,const void*b){double x=*(double*)a,y=*(double*)b;return (x>y)-(x<y);}
#ifndef RB
#define RB 8
#endif
int main(){
  int h=128,x=262,K=h+x,N=4*h;
  float*W=malloc(4*K*N),*in=malloc(4*K),*z=malloc(4*N);
  for(int i=0;i<K*N;i++)W[i]=((i*2654435761u)%1000)/1e5f;
  int Ts[]={10,50,100,200,400},REP=21;
  printf("T,recurrent_ms,parallel_ms,ratio\n");
  for(int ti=0;ti<5;ti++){int T=Ts[ti];
    float*X=malloc(4*T*K),*Y=malloc(4*T*N),*c=calloc(h,4),*hh=calloc(h,4);
    for(int i=0;i<T*K;i++)X[i]=0.01f*(i%11);
    double ra[21],rb[21];
    for(int r=0;r<REP;r++){
      memset(c,0,h*4);memset(hh,0,h*4);double t0=now();
      for(int t=0;t<T;t++){
        memcpy(in,X+(size_t)t*K,x*4);memcpy(in+x,hh,h*4);
        for(int n=0;n<N;n++)z[n]=0;
        for(int k=0;k<K;k++){float v=in[k];const float*w=W+(size_t)k*N;for(int n=0;n<N;n++)z[n]+=v*w[n];}
        #ifndef NOELEM
        for(int j=0;j<h;j++){float i_=sg(z[j]),f=sg(z[h+j]),g=tanhf(z[2*h+j]),o=sg(z[3*h+j]);c[j]=f*c[j]+i_*g;hh[j]=o*tanhf(c[j]);}
#else
        for(int j=0;j<h;j++)hh[j]=z[j];
#endif
      }
      ra[r]=now()-t0;t0=now();
      for(int t0_=0;t0_<T;t0_+=RB){int rb_=(T-t0_<RB)?T-t0_:RB;
        for(int q=0;q<rb_;q++){float*y=Y+(size_t)(t0_+q)*N;for(int n=0;n<N;n++)y[n]=0;}
        for(int k=0;k<K;k++){const float*w=W+(size_t)k*N;
          for(int q=0;q<rb_;q++){float v=X[(size_t)(t0_+q)*K+k];float*y=Y+(size_t)(t0_+q)*N;for(int n=0;n<N;n++)y[n]+=v*w[n];}}}
      for(int t=0;t<T;t++)
#ifndef NOELEM
      for(int j=0;j<h;j++){float i_=sg(Y[t*N+j]),f=sg(Y[t*N+h+j]),g=tanhf(Y[t*N+2*h+j]),o=sg(Y[t*N+3*h+j]);float c_=f*0.5f+i_*g;Y[t*N+j]=o*tanhf(c_);}
#endif
      
      rb[r]=now()-t0;
    }
    qsort(ra,REP,8,cmp);qsort(rb,REP,8,cmp);
    printf("%d,%.3f,%.3f,%.2f\n",T,ra[REP/2],rb[REP/2],ra[REP/2]/rb[REP/2]);
  }
}
