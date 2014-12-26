from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

"""

# BORE (best or rest)

Input:

+ A list of _o(loves,hates,decisions)_. 
+ Where _decisions_ are a dictionary of _(key,value)_.

Output:

+ The _(key,value)s_, sorted by the probablity
  that this _(key,vaue)_ appears in the top
  _enough_  scoring items.
+ The actually probability _p_ is computed
  via _b**2/(b+r)_ where _b,r_ are the frequencies
  that _(key,value)_ appears in best or rest.

"""
def bestOrRest(log, enough=0.2, e=0.001):
  n1 ,n2  = len(log[0].like), len(log[0].dislike)
  lo1,hi1 = [ 10**32] * n1, [-10**32] * n1
  lo2,hi2 = [ 10**32] * n2, [-10**32] * n2  
  enough  = int(len(log) * enough)
  def fromHell(likes,dislikes):
    n, all = 0, 0
    for like in likes:
      n   += 1
      all += (0 - like)**2
    for dislike in dislikes:
      n   += 1
      all += (1 - dislike)**2
    return all**0.5 / n**5
  def norms(lst,lo,hi): 
    return [ (v - lo[n]) / (hi[n] - lo[n] + e)
             for n,v in enumerate(lst) ]
  def lohi(lst,lo,hi):
    for n,v in enumerate(lst):
      lo[n] = min(v, lo[n])
      hi[n] = max(v, hi[n])
  for one in log:
    lohi(one.like, lo1, hi1)
    lohi(one.dislike, lo2, hi2)
  for one in log:
    one.score= fromHell(norms(one.like,   lo1,hi1),
                        norms(one.dislike,lo2,hi2))
  log = sorted(log, key = lambda one: one.score)
  return log[-enough:],log[: -enough]

def bore(log, e=0.00001):
  best,rest = bestOrRest(log)
  def kvCounts(lst):
    counts,n = {},len(lst)
    for one in lst:
      for k,v in one.items():
        counts[(k,v)]= counts.get((k,v),0) + 1) / n
    return counts 
  scores = []
  nr, nb = len(rest), len(best)
  better = kvCounts(best)
  worse  = kvCounts(rest)
  for k,s1 in in better.items():
    s2 = worse.get(k,e)
    s1 = s1 * nb / (nr + nb)
    s2 = s2 * nr / (nr + nb)
    if s1 > s2:
       scores += [(s1**2 / (s1 + s2),k)]
  return sorted(scores,reverse=True)
    

