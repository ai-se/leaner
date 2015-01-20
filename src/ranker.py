from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

import housing,ranges
from rangesLib import *

d=housing.data()["data"]

n=len(d[0])
m=len(d)
q=int(m*0.25)
b4=Counts(map(lambda l:l[-1],d))

for i in range(n):
  r = sorted(ranges.sdiv(d,tiny=20,
                                       num1=lambda x:x[i]),
                           reverse=True,
                           key=lambda x:x[2])
  sd0,l0,mu0=r[0]; sd0,mu0=g([sd0,mu0])
  sd1,l1,mu1=r[1]; sd1,mu1=g([sd1,mu1])
  print(i,dict(mu0=mu0,mu1=mu1,diff=mu0-mu1,rel=int(100*(mu0-mu1)/mu1),sd0=sd0,sd1=sd1))