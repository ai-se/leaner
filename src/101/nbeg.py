from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from nb import *

@go
def _nb1():
  NB(enough=2)
  nb("weather.csv")

#@go
def _nb2():  nb("housingD.csv")
