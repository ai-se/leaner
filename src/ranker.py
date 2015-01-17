from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True


import housing,ranges

class Counts(): # Add/delete counts of numbers.
    def __init__(i,inits=[]):
      i.zero()
      for number in inits: i + number 
    def zero(i): i.n = i.mu = i.m2 = 0.0
    def sd(i)  : 
      if i.n < 2: return i.mu
      else:       
        return (max(0,i.m2)*1.0/(i.n - 1))**0.5
    def __add__(i,x):
      i.n  += 1
      delta = x - i.mu
      i.mu += delta/(1.0*i.n)
      i.m2 += delta*(x - i.mu)

def g(lst,n=0):
  return map(lambda x:round(x,n),lst)
  
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