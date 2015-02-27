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
  with settings(TABLE,era = 10):
    for t,rows,era in eras("housing.csv"):
      for row in rows:
        print(era,row)
    print("Indep",t.indep)
    for indep in t.indep:
      print(indep)

