from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

"""

# Simple Differential Evolution

"""
from column import *

def de(pop,log=None,score=None,cf=0.3,f=0.5):
  score = score or eval1
  def makeLog():
    nbad  = len(pop[0].bad)
    ngood = len(pop[0].good) 
    return o(good= [N() for _ in range(ngood)],
             bad = [N() for _ in range(nbad)])
  log = log or makeLog()
  def fromHell(one):
    n, all = 0, 0
    for v,t in zip(one.good,log.good):
      v    = t.norm(v)
      n   += 1
      all += (0 - v)**2
    for v,t in zip(one.bad, log.bad):
      v    = t.norm(v)
      n   += 1
      all += (1 - v)**2
    return all**0.5 / n**0.5
  def objScore(one):
    if not one.has('score'):
      one.good, one.bad = score(one.decisions)
      for v,t in zip(one.good + one.bad,
                     log.good + log.bad):
        t.tell(v)
      
      one.score = fromHell(one)
    return one.score
  def smear(d1,d2,d3):
    tmp={}
    for k in d1:
      v1 = d1[k]
      if r() < cf:
        v2 = d2[k] if k in d2 else v1
        v3 = d3[k] if k in d3 else v2
        v1 = v2 if f < r() else v3
      tmp[k] = v1
    return tmp
  pop = shuffle(pop)
  for n,old in enumerate(pop): 
    new  = o(decisions = smear(ask(pop).decisions,
                               ask(pop).decisions,
                               ask(pop).decisions))
    olds = objScore(old)
    news = objScore(new)
    if news > olds:
      pop[n] = new
  return pop,log