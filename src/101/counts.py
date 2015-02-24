from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

"""

# Counting Stuff

Counting maths and symbols

"""
from lib import *
import math


class S(): 
  def __init__(i,inits=[]):
    i.n,i.counts,i._also = 0, {}, None
    map(i.__iadd__,inits)
  def __iadd__(i,z): return i.inc(z,  1)
  def __isub__(i,z): return i.inc(z, -1)
  def inc(i,z,n):
    i._also = None
    i.n += n
    i.counts[z] = i.counts.get(z,0) + n
    return i
  def norm(i,z): return z
  def like(i,z):
    return i.counts.get(z,0) / i.n
  def most(i): return i.also().most
  def mode(i): return i.also().mode
  def ent(i) : return i.also().e
  def __repr__(i): return str(i.also())
  def also(i):
    if not i._also:
      e,most,mode = 0,0,None
      for z in i.counts:
        if i.counts[z] > most:
          most,mode = i.counts[z],z
        p = i.counts[z]/i.n
        if p: 
          e -= p*math.log(p,2)
      i._also = o(counts=i.counts,
                  most=most,mode=mode,e=e)
    return i._also

# too many calls to hi lo sd for incremental
class N(): 
  def __init__(i,inits=[]):
    i._also  = None
    i.sample = Sample()
    i.n = i.mu = i.m2 = i.sd = 0
    map(i.__iadd__,inits)
  def sd(i) : return i.also().sd
  def lo(i) : return i.also().lo
  def hi(i) : return i.also().hi
  def norm(i,x):
    return (x - i.lo()) / (i.hi() - i.lo() +0.0001)
  def like(i,x):
    print("x",x,i,my,i.sd())
    return normpdf(i.mu, i.sd(),x)
  def __iadd__(i,x):
    i._also   = None
    i.sample += x
    i.n      += 1
    print(x,i.mu)
    delta     = x - i.mu
    i.mu     += delta/i.n
    i.m2     += delta*(x - i.mu)
    return i
  def __isub__(i,x):
    i._also = None; i.sample = Sample()
    i.n    -= 1
    delta   = x - i.mu
    i.mu   -= delta/i.n
    i.m2   -= delta*(x - i.mu)
    return i
  def __repr__(i): return str(i.also())
 
  
def cliffsDelta(lst1,lst2,dull=None):
  if dull is None: dull = the.COUNT.dull
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

def ntiles(lst,tiles):
  thing = lambda z: lst[ int(len(lst)*z)  ]
  return [ thing(tile) for tile in tiles ]

def ranked(d,tiles=None):
  "Returns a ranked list."
  tiles = tiles or the.COUNT.tiles
  def prep(key):
    nums  = sorted(d[key])
    med,iqr = median(nums)
    return o(rank  = 1,
             name  = key,
             _nums = nums,
             median= med,
             iqr   = iqr,
             tiles = ntiles(nums, tiles))
  lsts = sorted([prep(k) for k in d],
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
