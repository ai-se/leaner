from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from table import *

@setting
def NB(**d): 
  return o(
    m = 2,
    k = 1
  ).add(**d)


  
def nb(f):
  def known(row):
    pos   = t.klass[0].col
    klass = row[pos]
    if not klass in klasses:
      klasses[klass] = header(table0(),t.spec)
    return klass, klasses[klass]  
  t       = table0()
  klasses = {}
  n       = 0
  for row in era(f,t):
    n  += 1
    klass, about = known(row)
    
    Row(row.cells,about)
  for one in t.indep:
    print("")
    for key in klasses:
      head = klasses[key].all[one.col]
      print(one.name,key,head)







    
