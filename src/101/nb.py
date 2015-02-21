from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from table import *


def nb(f):

@setting
def NB(**d): 
  return o(
    m = 2,
    k = 1
  ).add(**d)

def nb(f):
  t       = table0()
  klasses = {}
  def known(row):
    pos   = t.klass[0].col
    klass = known(row[pos])
    if not klass in klasses:
      klasses[klass] = header(table0(),t.spec)
    return klass, klasses[klass]
  n = 0
  for row in era(f,t):
    n    += 1
    klass, about = known(row)
    
    tell(row,klass) # train
    
      
    
