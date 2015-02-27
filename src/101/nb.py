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
  n, klasses = 0,{}
  for t,row in era(f):
    n += 1
    actual, aboutActual = nbAbout(t,klasses,row)
    # switch to eras as soon s you can
    if n > the.NB.enough:
      predicted = nbClassify(klasses,n,row)
      log.tell(actual, predicted)
    nbTrain(row.cells,aboutActual)
  log.ask()
 
def nbTrain(cells, about):
   Row(cells,about)
   
def nbClassify(klasses,n,row):
  m = the.NB.m
  k = the.NB.k
  guess, best, nh = None, -10**32, len(klasses)
  for x in klasses:
    aboutx = klasses[x]
    prior  = (aboutx.n + k ) / (n + k * nh)
    like   = log(prior)
    for y,hdr in cells(row, aboutx.inSym):
      like += log((hdr.cnt(y) + (m*prior)) / (aboutx.n+m))
    for y,hdr in cells(row, aboutx.inNum):
      like += log(hdr.pdf(y))
    if like > best:
      guess, best = x, like
  return guess

def nbReport(t,klasses):
  for one in t.indep:
    print("")
    for key in klasses:
      head = klasses[key].all[one.col]
      print(one.name,key,head)

def nbAbout(t,klasses,row):
   pos = t.klass[0].col
   x   = row[pos]
   if not x in klasses:
     klasses[x] = header(t.spec,table0())
   aboutx = klasses[x]
   return x, aboutx





    
