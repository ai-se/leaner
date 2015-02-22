# -*- python -*-

from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

from counts import *

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
      approximation = Sample(truth,size=size).all
      out += [ldiff(truth, approximation)]
    print(exps,'times, approximate', n,
          'values from', f.__name__,
          'with a cache of size',
          size, q(sorted(out)), '% error')

@go
def _S():
  s=S()
  for x in list('tell.us.what.we.do.not.know'):
    s += x
  print(s.also())

@go
def _N():
  n=N()
  for x in xrange(10):
    n += x
  print( abs(n.sd-3.0276503541) < 10**-9)

@go
def _ranked():
  def worker(d):
    for one in ranked(d):
      print(one)
  print("\nbasic..............:"); worker({
       "rx1": [1,1,1,1,1,1,1,1],
       "rx2": [2,2,2,2,2,2,2,2]})
  print("\nstandard...........:"); worker({
       "rx1": [0.34, 0.49, 0.51, 0.6],
       "rx2": [0.6,  0.7,  0.8,  0.9],
       "rx3": [0.6,  0.7,  0.8,  0.9],
       "rx4": [0.1,  0.2,  0.3,  0.4]})
  print("\nall the same.......:"); worker({
      "rx1": [101, 100, 99, 101,  99], 
      "rx2": [101, 100, 99, 101, 100],
      "rx3": [101, 100, 99, 101,  99],
      "rx4": [101, 100, 99, 101, 100],
      "rx5": [101, 100, 99, 101,  99],
      "rx6": [101, 100, 99, 101, 100]})
  print("\ntwo large seperated:"); worker({
       "rx1": [101, 100,  99, 101,  99],
       "rx2": [101, 100, 199, 101, 100],
       "rx3": [101, 100, 199, 101, 199],
       "rx4": [401, 400, 400, 401, 401, 510],
       "rx5": [401, 400, 499, 401, 490, 520],
       "rx6": [401, 400, 499, 401, 410, 530] })
  print("\nvery small bags....:");worker({
       "rx1": [1],
       "rx2": [2],
       "rx3": [3],
       "rx4": [1000]})

