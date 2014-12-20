from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

"""

# General stuff (demos)

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
  print('one',one,'two',two)
"""

## Stats stuff

"""
seed(1)
lst1=[r() for _ in xrange(1000)]
lst2=[r()**1.2 for _ in xrange(1000)]
print('big difference:',
      1==cliffsDelta(lst1,lst2))
lst3=[r() for _ in xrange(1000)]
print('small difference:',
      0==cliffsDelta(lst1,lst2))
"""

## Printing stuff

"""
