from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True
"""

# Counting Stuff

Counting maths and symbols

"""
from lib import *
import math

@setting
def COUNT(**d): return o(
    # Thresholds are from http://goo.gl/25bAh9
    dull = [0.147, 0.33, 0.474][0],
    tiles = [0.25, 0.5, 0.75 ]
    )
"""

## Keeping Counts of Symbols

"""
class S(): 
  def __init__(i,inits=[]):
    i.n,i.counts  = 0, {}
    i.mode, i.most = None, 0
    map(i.__iadd__,inits)
  def __iadd__(i,z): return i.inc(z,  1)
  def __isub__(i,z): return i.inc(z, -1)
  def inc(i,z,n):
    i.n += n
    tmp = i.counts[z] = i.counts.get(z,0) + n
    if tmp > i.most:
      i.most, i.mode = tmp,z
    return i
  def norm(i,z):
    return z
  def __repr__(i):
    return str(o(mode = i.mode, most=i.most,
                 n=i.n,counts=i.counts))
  def e(i):
    e = 0
    for z in i.counts:
      p = i.counts[z]/i.n
      if p: 
          e -= p*math.log(p,2)
    return e
"""

## Keeping Counts of Numbers

"""
class N(): 
  def __init__(i,inits=[]):
    i.n = i.mu = i.m2 = 0
    i.lo = 10**32; i.hi = -1*i.lo
    map(i.__iadd__,inits)
  def norm(i,x):
    return (x - i.lo()) / (i.hi() - i.lo() +0.0001)
  def sd(i):
    return 0 if i.n < 2 else (i.m2/(i.n - 1))**0.5
  def __iadd__(i,x):
    i.n   += 1
    i.lo   = min(i.lo, x)
    i.hi   = max(i.hi, x)
    delta  = x - i.mu
    i.mu  += delta/i.n
    i.m2  += delta*(x - i.mu)
    return i
  def __isub__(i,x):
    i.n    -= 1
    delta   = x - i.mu
    i.mu   -= delta/i.n
    i.m2   -= delta*(x - i.mu)
    return i
  def __repr__(i):
    return str(o(n=i.n, mu=i.mu,sd = i.sd(),
                 lo=i.lo, hi=i.hi))
"""

## Cliff's Delta

Checking if the two lists of numbers are
different by an interesting amount.

""" 
def cliffsDelta(lst1,lst2,dull=None):
  dull = dull or the.COUNT.dull
  m, n = len(lst1), len(lst2)
  lst2 = sorted(lst2)
  j = more = less = 0
  for repeats,x in runs(sorted(lst1)):
    while j <= (n - 1) and lst2[j] <  x: 
      j += 1
    more += j*repeats
    while j <= (n - 1) and lst2[j] == x: 
      j += 1
    less += (n - j)*repeats
  d= (more - less) / (m*n + 0.000001) 
  return abs(d)  > dull
"""

Take a dictionary of values representing
different treatments. Return a list
of the values, sorted on their median,
ranked by Cliff's Delta.

"""
def ranked(rx,tiles=None):
  "Returns a ranked list."
  tiles = tiles or the.COUNT.tiles
  def prep(key):
    nums  = sorted( rx[key] )
    med,iqr = median(nums)
    return o(rank  = 1,
             name  = key,
             _nums = nums,
             median= med,
             iqr   = iqr,
             tiles = ntiles(nums, tiles))
  lsts = sorted([prep(k) for k in rx],
                key = lambda z: z.median)
  rank, pool = 1, []
  for x in lsts:
    if cliffsDelta(x._nums, pool):
      rank += 1
      pool  = x._nums
    else:
      pool += x._nums
    x.rank = rank
  return lsts
