from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from table import *

@go
def _rows():
  n=0
  for row in rows("housing.csv"):
    n += 1
    print(row)
    if n > 50: return

@go
def _era():
  the.TABLE.era = 10
  the.TABLE.want = 50
  t=table0()
  print(t)
  for row in era("housing.csv",t):
    print(row)

