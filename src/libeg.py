from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

"""

# General stuff (demos)

"""
from lib import *
"""

## Random stuff

"""
def lst(): return list('0123456789')

seed(1)
l1= shuffle(lst())
print(l1)
print(shuffle(lst()))
seed(1)
l2=shuffle(lst())
print('Resetting seed replicated old results:',
    l1==l2)
"""

## Iterator stuff

"""
for one,two in pairs(lst()):
  print('pairs of one',one,' and two',two)
"""

## Stats stuff

"""
seed(1)
lst1=[r() for _ in xrange(1000)]
print('big difference:',
      1==cliffsDelta(
        lst1,
        [r()**2 for _ in xrange(1000)]))
print('small difference:',
      0==cliffsDelta(
        lst1,
        [r() for _ in xrange(1000)]))
"""

## Printing stuff

"""
