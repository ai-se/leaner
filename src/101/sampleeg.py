# -*- python -*-

from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

from sample import *
			   
def any(lst):
  return lst[ int(r() * len(lst)) ]

def q(lst,n=[0.1,0.3,0.5,0.7,0.9],g=3):
  lst = sorted(lst)
  m =  len(lst)
  return [round(100*lst[int(m*i)]) for i in n]

def ldiff(l1,l2,n=1000):
  diff, l3,l4 = 0, [],[]
  for _ in xrange(n):
    l3 += [ any(l1) ]
    l4 += [ any(l2) ]
  for n1,n2 in zip( sorted(l3),sorted(l4) ):
    diff += n2 - n1
  return diff/(sum(l1)+0.00001)

def sample1(lst,f,a,b):
  try:
    lst += [f(a,b)]
  except:
    return None
  
def _samples(n=1000,exps=128):
  rseed(1)
  g = lambda z: '%2g' % z
  lst = [r() for _ in xrange(n)]
  print('%g' % (100*ldiff(lst,lst)))
  f     = random.weibullvariate
  for size in [16,32,64,128,256,512]:
    out = []
    for _ in xrange(exps):
      alpha = r()*1000
      beta  = r()*10
      truth = []
      for _ in xrange(n):
        sample1(truth,f,alpha,beta)
      approximation = Sample(truth,size=size).all()
      out += [ldiff(truth, approximation)]
    print(exps,'times i approximated',n,'values from a',f.__name__,'distribution in a cache of size and got ',size,q(out),'% error')

_samples()
 
