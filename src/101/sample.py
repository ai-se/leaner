from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

"""

# Sampling

Keep some random subset of a set of items.

"""
from lib import *

@setting
def SAMPLE(**d): 
  return o(
    cache = 128
    ).add(**d)
"""

## Sample

`Sample` holds the cache and, if asked will compute 
(and keep) the `median` and `lo,hi` of the cached values

"""
class Sample:
  def __init__(i,init=[],size=None):
    i._also = None
    i.cache = Cache(init,size)
  def __iadd__(i,x):
    i._also = None
    i.cache += x
    return i
  def all(i): return i.cache.all
  def also(i):
    if not i._also:
      i._also= o(
        n  = i.n, 
        med= None, iqr= None,  lo= None, hi= None)
      i.cache.all.sort()
      if i.cache.all:
        i._also.lo  = i.cache.all[ 0]
        i._also.hi  = i.cache.all[-1]
        med, iqr    = median(i.cache.all)
        i._also.med = med
        i._also.iqr = iqr 
    return i._also
"""

## Cache

Throw lots of things at a `Cache`, keep some of them.

"""
class Cache:
  def __init__(i,init=[],size=None):
    i.size = size or the.SAMPLE.cache
    i.max, i.all, i.n = size, [], 0
    map(i.__iadd__,init)
  def __iadd__(i,x):
    i.n += 1
    now  = len(i.all)
    if now < i.max:
      i.all += [x]
    elif r() <= now/i.n:
      i.all[ int(r() * now) ]= x
    return i

