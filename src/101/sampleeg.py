from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

"""

# Demo of Sampling

How many random samples of a distribution do we need to approximate
that distribution? This code generates mulitple distributions
(by selecting random `shape` and `scale` parameters to
the `weibull` function). For each distribution:

+ Many times:
  + Pull, say, 1000 numbers (call it `truth`);
  + Save some random subset into a `Sample` of some `size` 
    (call it the `approximation`);
  + Then pull the same number of randomly selected items
    from `truth` and `approximation`.
  + Sort the pulled values and compute the error difference
    between the _i-th_ item of each pull values.
  + Report this error as a percentage of `truth`.

"""

from sample import *
		 
@go
def _samples(n= 512, exps= 50, seed=1,
             f= random.weibullvariate):
  def sample1(lst,a,b):
       try   : lst += [f(a,b)]
       except: return None
  def show(x): return int(abs(round(100*x)))
  def q(lst,n=[0.1,0.3,0.5,0.7,0.9],g=3):
       "Return the n-th percentile items"
       m  = len(lst)
       return [ show(lst[int(m*i)]) for i in n]
  def ldiff(l1,l2,n=1000):
       "Find %delta between samples of size 'n'"
       def any(lst):
         return lst[ int(r() * len(lst)) ]
       diff, l3,l4 = 0, [],[]
       for _ in xrange(n):
         l3 += [ any(l1) ]
         l4 += [ any(l2) ]
       for n1,n2 in zip( sorted(l3),sorted(l4) ):
         diff += n2 - n1
       return diff/(sum(l1)+0.00001)
  rseed(seed)
  for size in [25,50,100,200]:
    out = []
    for _ in xrange(exps):
      alpha = r()*1000
      beta  = r()*10
      truth = []
      for _ in xrange(n):
        sample1(truth,alpha,beta)
      approximation = Sample(truth,size=size).all()
      out += [ldiff(truth, approximation)]
    print(exps,'times, approximate', n,
          'values from', f.__name__,
          'with a cache of size',
          size, q(sorted(out)), '% error')
