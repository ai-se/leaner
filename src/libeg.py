from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

"""

# General stuff (demos)

"""
from lib import *

def lst(): return list('0123456789')

@go
def _lists():
  "Random stuff"
  
  seed(1)
  l1= shuffle(lst())
  print(l1)
  print(shuffle(lst()))
  seed(1)
  l2=shuffle(lst())
  print('Resetting seed replicated old results:',
        l1==l2)

@go
def _pairs():
  "Walk thru pairs of the list."
  for one,two in pairs(lst()):
    print('pairs of one',one,' and two',two)

@go
def _cliffsDelta():
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

@go
def _g():
  lst = [r() for _ in xrange(20)]
  print(lst)
  print(g(lst))

@go
def _printm():
  "Pretty print columns of text."
  text="""Lorem ipsum dolor sit amet, consectetur adipiscing
  elit, sed do eiusmod tempor incididunt ut labore et
  dolore magna aliqua. Ut enim ad minim veniam, quis
  nostrud exercitation ullamco laboris nisi ut aliquip
  ex ea commodo consequat. Duis aute irure dolor in
  reprehenderit in voluptate velit esse cillum dolore
  eu fugiat nulla pariatur. Excepteur sint occaecat
  cupidatat non proident, sunt in culpa qui officia 
  deserunt mollit anim id est laborum."""
  m= [line.split() for line in text.splitlines()]
  printm(m)

@go
def _xtile():
  "Percentile print of numbers."
  def raisedTo(n):
    lst=[r()**n for _ in xrange(1000)]
    print(n,": ",xtile(lst,lo=0,hi=1,show="%3.2f"))
  raisedTo(0.5)
  raisedTo(1.0)
  raisedTo(2.0)
  

