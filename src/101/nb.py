from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from table import *
from abcd  import *

@setting
def NB(**d): 
  return o(
    m = 2,
    k = 1,
    enough=10,
  ).add(**d)

def nb(f):
  log = Abcd()
  n, klasses, t = 0,{},table0()
  for row in era(f,t):
    n += 1
    actual, about = nbKnown(t,klasses,row)
    if n > the.NB.enough:
      print(about.dep[0].counts)
      predicted = nbTest(t,klasses,n,row)
      log.tell(actual, predicted)
    Row(row.cells,about)
  nbReport(t,klasses)

def nbTest(t,klasses,n,row):
  guess,best = None,-1
  for klass, about in klasses.items():
    like = about.n/n
    for indep in t.indep:
      val = row[indep.col]
      print("vall",val)
      if val is not the.TABLE.skip:
        like = like * indep.like(val)
    if like > best:
      guess, best = klass, like
  return guess
  
def nbTrain(cells,about):
  Row(cells,about)
  
def nbReport(t,klasses):
  for one in t.indep:
    print("")
    for key in klasses:
      head = klasses[key].all[one.col]
      print(one.name,key,head)

def nbKnown(t,klasses,row):
   pos   = t.klass[0].col
   klass = row[pos]
   if not klass in klasses:
     klasses[klass] = header(table0(),t.spec)
   return klass, klasses[klass]  





    