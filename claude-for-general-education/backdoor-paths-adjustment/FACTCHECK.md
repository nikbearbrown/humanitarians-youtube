# FACTCHECK — backdoor-paths-adjustment

- Backdoor criterion: block all paths entering T via back-arrow (Pearl 2009): correct.
- DAG with Brand, Comp, Quality each confounding T->Y: 3 backdoor paths correct.
- Adjustment set {Brand, Comp, Quality} blocks all 3 paths: correct.
- New edge Comp->Brand creates path T<-Brand<-Comp->Y: correct.
- Same adjustment set still blocks: Brand blocks path 1+4, Comp blocks path 2+4, Quality blocks path 3: correct.
