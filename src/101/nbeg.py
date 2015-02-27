from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

# test on diabestes

from nb import *

@go
def _nb1():
  with settings(NB,enough=2),settings(LIB,seed=2):
    nb("weather.csv")

#@go
def _nb2():  nb("housingD.csv")
