from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

from columns import *


@go
def _rows():
  for n,line in rows('../data/nasa93dem1.csv'):
    if n < 10:
      print(n,line)


@go
def _unzip1():
  for line in unzip('../data/data.zip','nasa93dem.csv'):
    print(line)

@go
def _unzip2():
  for line in rows('nasa93dem.csv',the.TBL.source):
    print(line)
