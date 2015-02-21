from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

from lib import *

@setting
def COUNT(**d): 
  def halfEraDivK(z): 
    return z.opt.era/z.opt.k/2
  return o(
    cache     = 128
    ).add(**d)

import random
r = random.random
rseed=random.seed

class Sample:
  def __init__(i,init=[],size=None):
    if size is None: size = the.COUNT.cache
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

class S(): 
  def __init__(i,inits=[]):
    i.n,i.count,i._also = 0, {}, None
    for number in inits: i += number 
  def __iadd__(i,z): return i.inc(z,  1)
  def __isub__(i,z): return i.inc(z, -1)
  def inc(i,z):
    i._also = None
    i.n += n
    i.counts[z] = i.counts.get(z,0) + n
    return i
  def most(i): return i.also().most
  def mode(i): return i.also().mode
  def ent(i) : return i.also().e
  def also():
    if not i._also:
      e,most.mode = 0,0,None
      for z in i.counts:
        if i.counts[z] > most:
          most,mode = i.counts[z],z
        p = i.counts[z]/i.n
        if p: 
          e -= p*math.log(p,2)
        i._also = o(most=most,mode=mode,e=e)
    return i._also
  
class N(): 
  def __init__(i,inits=[]):
    i.n = i.mu = i.m2 = i.sd = 0
    for number in inits: i += number 
  def _sd(i)  :
    if i.n > 1 :
      i.sd = (max(0,i.m2)*1.0/(i.n - 1))**0.5
    return i
  def __iadd__(i,x):
    i.n  += 1
    delta = x - i.mu
    i.mu += delta/(1.0*i.n)
    i.m2 += delta*(x - i.mu)
    return i._also()
  def __isub__(i,x):
    i.n  -= 1
    delta = x - i.mu
    i.mu -= delta/(1.0*i.n)
    i.m2 -= delta*(x - i.mu)
    return i._also()
