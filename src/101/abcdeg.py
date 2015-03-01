from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from lib  import *
from abcd import *

@go
def _abcd1():
  rseed(1)
  abcd = Abcd(db='randomIn',rx='jiggle')
  train = list('aaaaaaaabbbbbcc')
  test  = shuffle(train[:])
  for actual, predicted in zip(train,test):
    abcd(actual,predicted)
  abcd.report()

"""
output:
 $ python abcdeg.py 
==| _abcd |========================================

# db                   rx            n    a    b   c   d    acc pd  pf  prec f  g  class
----------------------------------------------------------------------------------------------------
# randomIn             jiggle        8    3    4   4    4   40  50  57  50  50  46 a
# randomIn             jiggle        2   11    2   2    0   40   0  15   0  50   0 c
# randomIn             jiggle        5    7    3   3    2   40  40  30  40  40  51 b   
"""

@go
def _abcd2():
  rseed(1)
  lst = [1,1,1,1,1,1,1,1,2,2]
  last = Abcd()
  for i in xrange(1,10):
    now = last.copy()
    for _ in xrange(50):
      now(any(lst),any(lst))
    s = now.scores()
    for k in s:
      print(i, k,s[k].a, s[k].b, s[k].c, s[k].d)
      break
    last = now
  
    
