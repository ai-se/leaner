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

d=housing.data()["data"]

n=len(d[0])
m=len(d)
q=int(m*0.25)
b4=Counts(map(lambda l:l[-1],d))

for i in range(n):
  for sd1,l1,mu1 in sorted(ranges.sdiv(d,tiny=20,
                                       num1=lambda x:x[i]),
                           reverse=True,
                           key=lambda x:x[2]):
    if mu1 > b4.mu:
      print(dict(i=i,b4=dict(mu=b4.mu,sd=b4.sd()),
                 now=dict(mu=mu1,sd=sd1)))
    break


