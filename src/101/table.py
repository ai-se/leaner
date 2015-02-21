from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from lib import *
from counts import *

@setting
def TABLE(**d): return o(
    num   = '$',
    int   = '!',
    klass = '=',
    skip  = "?",
    sep   = ',',
    bad   =  r'(["\' \t\r\n]|#.*)',
    era   = 256,
    want  = 1000
  ).add(**d)

import re
def rows(file):
  def what(z):
    if the.TABLE.num in z: return float
    if the.TABLE.int in z: return int
    return noop
  def whats(line):
    return [(col,what(name)) for col,name 
            in enumerate(line) 
            if not the.TABLE.skip in name]
  def lines(): 
    kept = ""
    for line in open(file):
      now   = re.sub(the.TABLE.bad,"",line)
      if now:
        kept += now
        if kept:
          if not now[-1] == the.TABLE.sep:
            yield kept.split(the.TABLE.sep)
            kept = "" 
  todo = None
  for line in lines():
    if todo:
      yield [ comp(line[col]) for col,comp in todo ]
    else:
      todo = whats(line)
      yield line
"""

## The Era Pattern

Run over the data using a window of size _era_.  For
each era, shuffle the data order. Return one row at
a time. Flag if this is the first row. Return 
at least _want_ number of rows.

"""
def era(file,t,n=0):
  def chunks():
    chunk = []
    for row in rows(file):
      if not t.all:
        header(row,t)
      else:
        data(row,t)
        chunk += [row]
        if len(chunk) >= the.TABLE.era:
          yield chunk
          chunk=[]
    if chunk: yield chunk
  for chunk in chunks():
    for row in shuffle(chunk):
      n += 1
      yield row
      if n >= the.TABLE.want: return
  if n < the.TABLE.want:
    for row in era(file,t,n):
      yield row
"""

## The Table Pattern

The first row contains header info. All other rows are data.
Yield all rows, after updating header and row data information.

"""
def table0():
  return o(num=[],sym=[],ord=[],
           more=[],less=[],
           name={},index={},
           indep=[],dep=[],all=[])

def data(row,t):
  for about,cell in zip(t.all,row):
    about += cell
  return row

def header(row,t):
  tbl = the.TABLE
  def what(z):
    return (N,t.num) if tbl.num in z else (S,t.sym)
  def depOrindep(z,header):
    where  = t.dep if tbl.klass in z else t.indep
    where += [header]
  def moreOrLess(z,header,t):
    if tbl.more in z : t.more.append(header)
    if tbl.less in z : t.less.append(header)
  for col,name in enumerate(row):
    t.name[col]  = name
    t.index[name] = col
    print(col,name)
    header, where = what(name)
    header.name   = name
    where        += [header]
    depOrindep(name,header)
    moreOrLess(name,header,t)
    t.all += [header]
  return t
