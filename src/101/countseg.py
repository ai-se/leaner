# -*- python -*-

from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

from counts import *

@go
def _S():
  s=S()
  for x in list('tell.us.what.we.do.not.know'):
    s += x
  print(s)

@go
def _N():
  n=N()
  for x in xrange(10):
    n += x
  print( abs(n.sd() - 3.0276503541) < 10**-9)

@go
def _ranked():
  def worker(d):
    for one in ranked(d):
      print(one)
  print("\nbasic..............:"); worker({
        "rx1": [1,1,1,1,1,1,1,1],
        "rx2": [2,2,2,2,2,2,2,2]})
  for t in [0.01,0.3]:
    with settings(COUNT,trivial=t):
      print("\nstandard...........:",the.COUNT.trivial)
      worker({
        "rx1": [0.34, 0.49, 0.51, 0.6],
        "rx2": [0.6,  0.7,  0.8,  0.9],
        "rx3": [0.6,  0.7,  0.8,  0.9],
        "rx4": [0.1,  0.2,  0.3,  0.4]})
  
  print("\nall the same.......:"); worker({
       "rx1": [101, 100, 99, 101,  99], 
       "rx2": [101, 100, 99, 101, 100],
       "rx3": [101, 100, 99, 101,  99],
       "rx4": [101, 100, 99, 101, 100],
       "rx5": [101, 100, 99, 101,  99],
       "rx6": [101, 100, 99, 101, 100]})
  with settings(COUNT,trivial=1):
    print("\ntwo large separated:",the.COUNT.trivial)
    worker({
        "rx1": [101, 100,  99, 101,  99],
        "rx2": [101, 100, 199, 101, 100],
        "rx3": [101, 100, 199, 101, 199],
        "rx4": [401, 400, 400, 401, 401, 510],
        "rx5": [401, 400, 499, 401, 490, 520],
        "rx6": [401, 400, 499, 401, 410, 530] })
  print("\nvery small bags....:");worker({
        "rx1": [1],
        "rx2": [2],
        "rx3": [3],
        "rx4": [1000]})

