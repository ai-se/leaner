
<small>_This file is part of LEANER. To know more, view the source code [bore.py](../src/bore.py) or read our [home](https://github.com/ai-se/leaner) page._</small>



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

````python
def bestOrRest(log, enough=0.2, e=0.001):
  n1 ,n2  = len(log[0].good), len(log[0].bad)
  lo1,hi1 = [ 10**32] * n1, [-10**32] * n1
  lo2,hi2 = [ 10**32] * n2, [-10**32] * n2  
  enough  = int(len(log) * enough)
  def fromHell(goods,bads):
    n, all = 0, 0
    for v in goods:
      n   += 1
      all += (0 - v)**2
    for v in bads:
      n   += 1
      all += (1 - v)**2
    return all**0.5 / n**0.5
  def norms(lst,lo,hi): 
    return [ (v - lo[n]) / (hi[n] - lo[n] + e)
             for n,v in enumerate(lst) ]
  def lohi(lst,lo,hi):
    for n,v in enumerate(lst):
      lo[n] = min(v, lo[n])
      hi[n] = max(v, hi[n])
  for one in log:
    lohi(one.good, lo1, hi1)
    lohi(one.bad, lo2, hi2)
  for one in log:
    one.score= fromHell(norms(one.good,lo1,hi1),
                        norms(one.bad, lo2,hi2))
  log = sorted(log, key = lambda one: one.score,
               reverse=True)
  return log[:enough],log[enough:]

def bore(log, enough=0.25, e=0.00001):
  best,rest = bestOrRest(log, enough=enough)
  def kvCounts(lst):
    cnts = {}
    for one in lst:
      for x in one.decisions.items():
        cnts[x] = cnts.get(x,0) + 1
    return cnts 
  scores = []
  nr, nb = len(rest), len(best)
  better = kvCounts(best)
  worse  = kvCounts(rest)
  for k,s1 in better.items():
    s2 = worse.get(k,e)
    p1 = s1/nb * nb / (nr + nb)
    p2 = s2/nr * nr / (nr + nb)
    if p1 > p2:
       scores += [(p1**2 / (p1 + p2),k)]
  return sorted(scores,reverse=True)
    

````
