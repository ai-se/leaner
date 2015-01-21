from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

import housing,ranges
from rangesLib import *

t=housing.data()
d= t["data"]
n= t["names"]

n=len(d[0])
m=len(d)
q=int(m*0.25)
b4=Counts(map(lambda l:l[-1],d))
r=[]
for i,name in zip(range(n),t["names"]):
  ranges.sdiv(d,attr=name,tiny=20,
            num1=lambda x:x[i],cuts=r)
r = sorted(r,key=lambda x :x.mu*-1)
for one in r[:5]:
    print(one.attr,
      one.lo, one.hi,one.mu,b4.mu)