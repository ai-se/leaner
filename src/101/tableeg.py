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
  t=table0()
  for row in era("housing.csv",t):
    print(row)
  for indep in t.indep:
    print(indep)

