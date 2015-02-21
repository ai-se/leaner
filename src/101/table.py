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
    more  = '>',
    less  = '<',
    bad   =  r'(["\' \t\r\n]|#.*)',
    era   = 256
  ).add(**d)

### continuations are not at the thing level

import re
def rows(file):
  def what(z):
    if the.TABLE.num in z: return float
    if the.TABLE.int in z: return int
    return noop
  def todos(line):
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
      line = [ comp(line[col]) for col,comp in todo ]
    else:
      todo = todos(line)
    yield line
"""

## The Era Pattern

Run over the data using a window of size _era_.  For
each era, shuffle the data order. Return one row at
a time. Flag if this is the first row. Return 
at least _want_ number of rows.

"""
def era(file,t):
  def chunks():
    chunk = []
    for row in rows(file):
      if not t.all:
        header(t,row)
      else:
        tell(t,row)
        chunk += [row]
        if len(chunk) >= the.TABLE.era:
          yield chunk
          chunk=[]
    if chunk: yield chunk
  for chunk in chunks():
    for row in shuffle(chunk):
      yield row

def tell(t,row):
  for one,x in zip(t.all,row): one += x
  return row
"""

## The Table Pattern

The first row contains header info. All other rows are data.
Yield all rows, after updating header and row data information.

"""
def table0():
  return o(num=[],sym=[],ord=[],spec=[],
           more=[],less=[],
           name={},index={},
           indep=[],dep=[],all=[])

def header(t,row):
  tbl = the.TABLE
  t.spec = row
  def what(z):
    if tbl.num in txt:
      return N(), t.num
    else:
      return S(), t.sym
  def dep(z) :
    if tbl.klass in z: return True
    if tbl.less  in z: return True
    if tbl.more  in z: return True
    return False
  for col,txt in enumerate(row):
    t.name[col]  = txt
    t.index[txt] = col
    header, at1 = what(txt)
    header.name = txt
    header.col  = col
    at1  += [header]
    at2   = t.dep if dep(z) else t.indep
    at2  += [header]
    if tbl.more in txt : t.more += [header]
    if tbl.less in txt : t.less += [header]
    t.all += [header]
  return t
