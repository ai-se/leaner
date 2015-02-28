from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from table import *
from abcd  import *

@setting
def NB(**d): 
  return o(
    m = 2,
    k = 1
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
      klasses[k] = header(t.spec)
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
  for this,klass in klasses.items():
    like = prior = (klass.n + k ) / (t.n + k * nh)
    for y,hdr in cells(row, klass.inSym):
      like *= (hdr.cnt(y) + (m*prior)) / (klass.n+m)
    for y,hdr in cells(row, klass.inNum):
      like *= hdr.pdf(y)
    if like > best:
      guess, best = this, like
  return guess



    
