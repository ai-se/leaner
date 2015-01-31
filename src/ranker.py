from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

import housing,ranges
from rangesLib import *

def g(x): return ('%g' % x)

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
            x=lambda z:z[i],cuts=r)
r = sorted(r,key=lambda z :z.y.mu*-1)
for one in r:
    if one.y.mu <= (b4.mu + b4.sd()):
      print(".",end="")
    else:
      print(one.attr, 
        one.x.lo, one.x.hi,g(one.y.mu),g(one.y.sd),g(b4.mu),g(b4.sd()),sep=",")