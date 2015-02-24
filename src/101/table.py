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
    era   = 256,
    shuffle=True
  ).add(**d)

class Row:
  id=0
  def __init__(i,cells=[],t=None):
    Row.id = i.id = Row.id + 1
    i.cells = cells
    i.table = t
    i.table.n += 1
    if t:
      for cell,value in zip(t.all,cells):
        if value is not the.TABLE.skip:
          cell += value
  def __getitem__(i,k): return i.cells[k]
  def __hash__(i)     : return i.id
  def __repr__(i): return '<'+str(i.cells)+'>'
  
import re
def rows(file):
  def use(z): return not the.TABLE.skip in z
  def what(z):
    if the.TABLE.num in z: return float
    if the.TABLE.int in z: return int
    return noop
  def todos(line):
    return [(col,what(name)) for col,name 
            in enumerate(line) if use(name)]
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
      line = [ txt for txt in line if use(txt)]
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
      print("era",row)
      if not t.all:
        header(t,row)
      else:
        chunk += [Row(row,t)]
        if len(chunk) >= the.TABLE.era:
          yield chunk
          chunk=[]
    if chunk: yield chunk
  for chunk in chunks():
    if the.TABLE.shuffle:
      chunk = shuffle(chunk)
    for row in chunk:
      yield row
"""

## The Table Pattern

The first row contains header info. All other rows are data.
Yield all rows, after updating header and row data information.

"""
def table0():
  return o(num=[],sym=[],ord=[],spec=[],
           more=[],less=[],klass=[],inSyms=[], inNum=[]
           name={},index={},n=0,
           indep=[],dep=[],all=[])

def header(t,row):
  tbl = the.TABLE
  t.spec = row
  def what(z):
    if tbl.num in txt:
      return N(), t.num
    else:
      return S(), t.sym
  def num(z):
    return isinstance(z,N)
  def dep(z) :
    return  tbl.klass in z or \
            tbl.less  in z or  \
            tbl.more  in z
  for col,txt in enumerate(row):
    t.name[col]  = txt
    t.index[txt] = col
    header, at1  = what(txt)
    header.name  = txt
    header.col   = col
    at1  += [header]
    at2   = t.dep if dep(txt) else t.indep
    at2  += [header]
    if tbl.klass in txt : t.klass += [header]
    if tbl.more  in txt : t.more  += [header]
    if tbl.less  in txt : t.less  += [header]
    t.all += [header]
    for z in i.indep:
      at3 = t.inNums if num(z) else t.inSym
      at3 += [header]
  return t
