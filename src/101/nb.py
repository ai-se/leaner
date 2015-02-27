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
      predicted = nbClassify(t,klasses,n,row)
      log.tell(actual, predicted)
    nbTrain(row.cells,about)
  nbReport(t,klasses)
 
def nbTrain(cells, about):
   Row(cells,about)
   
def nbClassify(t,klasses,n,row):
  m = the.NB.m
  k = the.NB.k
  guess, best, nh = None, -1, len(klasses)
  for x, klass in klasses.items():
    tmp = prior = (klass.n + k ) / (n + k * nh)
    for y,hdr in cells(row, klass.inSym):
      print(o(ako=klass.__name__, y=y,
              m=m, prior=prior, n=klass.n, tmp=tmp))
      tmp *= (hdr.cnt(y) + (m*prior)) / (klass.n+m)
    for y,hdr in cells(row, klass.inNum):
      tmp  *= head.pdf(y)
    if like > best:
      guess, best = x, like
  return guess

def nbReport(t,klasses):
  for one in t.indep:
    print("")
    for key in klasses:
      head = klasses[key].all[one.col]
      print(one.name,key,head)

def nbKnown(t,klasses,row):
   pos = t.klass[0].col
   x   = row[pos]
   if not x in klasses:
     klasses[x] = header(table0(),t.spec)
   return x,klasses[x]





    
