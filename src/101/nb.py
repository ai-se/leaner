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

def ilearn(src,test,train):
  log = Abcd()
  for t,rows,era in eras(src):
    for row in rows:
      k = theKlass(t,row)
      if era > 0:
        log(actual  = k,
            predict = test(t,row))
      train(t,row,k)
  return t,log

def nb(f):
  klasses = {}
  def train(t,row,k):
    if not k in klasses:
      klasses[k] = header(t.spec,table0())
    Row(row.cells, klasses[k])
  def test(t,row):    
    return nbClassify(t,row,klasses)
  t,log = ilearn(f,test,train)
  log.report()
  return t
   
def nbClassify(t,row,klasses):
  m = the.NB.m
  k = the.NB.k
  guess, best, nh = None, -10**32, len(klasses)
  for x in klasses:
    aboutx = klasses[x]
    like = prior  = (aboutx.n + k ) / (t.n + k * nh)
    for y,hdr in cells(row, aboutx.inSym):
      like *= (hdr.cnt(y) + (m*prior)) / (aboutx.n+m)
    for y,hdr in cells(row, aboutx.inNum):
      like *= hdr.pdf(y)
    if like > best:
      guess, best = x, like
  return guess



    
