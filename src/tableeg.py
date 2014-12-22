from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

from table import *


@go
def _rows():
  f = the.TBL.datafile('nasa93dem.csv')
  all = [line for n,line in rows(f) if n < 10]
  print(all)
