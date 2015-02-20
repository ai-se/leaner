from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

import random
r = random.random
rseed=random.seed

class Sample :
  def __init__(i,init=[],size=128):
    i.n=0
    i._kept = [None]*size
    map(i.__iadd__,init)
  def __iadd__(i,x):
    i.n += 1			     
    l    = len(i._kept)
    if r() <= l/i.n:
      i._kept[ int(r()*l) ]= x
  def all(i):
    return [x for x in i._kept
            if x is not None]
