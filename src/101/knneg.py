from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

# test on diabestes

from knn import *

@go
def _nb1():
  with settings(LIB,seed=2),settings(TABLE,era=3):
    knn("weather.csv")


#@go
def _nb1():
  with settings(LIB,seed=1),settings(TABLE,era=50):
    nb("housingD.csv")

#@go
def _nb2():  nb("housingD.csv")
