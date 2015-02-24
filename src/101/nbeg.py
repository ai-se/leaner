from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from nb import *

@go
def _nb1():
  NB(enough=2)
  nb("weather.csv")

#@go
def _nb2():  nb("housingD.csv")



def nbTest(t,cells,log,m=2,k=1):
  def theKlass(x)  : return x.classes[0]
  def theCount(h,x): return 1.0*h.counts.get(x,0)
  nh   = len(log.hs)
  most = The.ninf
  out  = None
  for h,counts in log.hs.items():
    klass = theKlass(counts)
    prior = (klass.n + k) * 1.0 / (log.n + k*nh)
    tmp   = prior
    for cell,num in obs(cells,counts.nums):
      tmp  *= normpdf(cell, num.mu, num.s)
    for cell,sym in obs(cells,counts.syms):
      f     = theCount(sym,cell) + (m*prior)
      tmp  *= f/(klass.n + m)
    if tmp > most:
      most,out = tmp , h
  log.abcd.keep(cells[klass.at],out)
