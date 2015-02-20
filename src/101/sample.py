from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

import random
r = random.random
rseed=random.seed

class Sample:
  def __init__(i,init=[],size=128):
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
