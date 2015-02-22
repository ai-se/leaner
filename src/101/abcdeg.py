from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from lib  import *
from abcd import *

@go
def _abcd():
  rseed(1)
  abcd = Abcd(db='randomIn',rx='jiggle')
  train = list('aaaaaaaabbbbbcc')
  test  = shuffle(train[:])
  for actual, predicted in zip(train,test):
    abcd.tell(actual,predicted)
  abcd.header()
  abcd.ask()

"""
output:
 $ python abcdeg.py 
# db                   rx           n     a    b    c   d    acc pd  pf  prec f  g  class     
----------------------------------------------------------------------------------------------------
# randomIn             jiggle       22    0    5    5   17   63  77 100  77  77   0 a         
# randomIn             jiggle        5   17    5    5    0   63   0  23   0  77   0 b       
"""
