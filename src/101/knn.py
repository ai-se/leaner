from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from learn import *

@setting
def KNN(**d): 
  return o(
    norm = True,
    k    = 1
  ).add(**d)

def knn(f):
  k = the.KNN.k
  klasses = {}
  rows = []
  def train(t,row,k):
    if not k in klasses:
      klasses[k] = header(t.spec)
    rows.append( Row(row.cells, klasses[k]) )
  def test(t,row):    
    return mode(
             theKlasses(
               nearest(k,row,rows)))
  t,logs = ilearn(f,test,train)
  ilearnReport(f,klasses,logs)
  return t

def nearest(k,row1,rows):
  dists= [ (row1.dist(row2), row2) for row2 in rows
            if id(row2) is not id(row1) ]
  return sorted(dists)[:k]
  

    
