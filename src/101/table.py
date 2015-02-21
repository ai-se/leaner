from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

@setting
def TABLE(**d): return o(
    num   = '$',
    ord   = '<',
    klass = '='
  ).add(**d)

@setting
def ROWS(**d): return o(
  skip="?",
  sep  = ',',
  bad = r'(["\' \t\r\n]|#.*)'
  ).add(**d)


def data(row):
  for col in w.num:
    val = row[col]
    w.min[col] = min(val, w.min.get(col,val))
    w.max[col] = max(val, w.max.get(col,val))



    
"""

## The Era Pattern

Run over the data using a window of size _era_.  For
each era, shuffle the data order. Return one row at
a time. Flag if this is the first row. Return 
at least _want_ number of rows.

"""
def era(file, n=0):
  def chunks():
    chunk = []
    for row in rows(file):
      chunk += [row]
      if len(chunk) > the.ERA.size:
        yield chunk
        chunk=[]
    if chunk: yield chunk
  for chunk in chunks():
    for row in shuffle(chunk):
      n += 1
      yield n==0,row
      if n > the.ERA.want: return
  if n < the.ERA.want:
    for first,row in era(file,n):
      yield first,row
"""

## The Table Pattern

The first row contains header info. All other rows are data.
Yield all rows, after updating header and row data information.

"""
def table(file):
  t= t or o(nums=[],sym[],ords=[])
  for first, row in era(file):
    if first:
      header(row,t)
    else:
      data(row,t)
      yield t,row

def header(row,t):
  def numOrSym(val):
    return w.num if w.opt.num in val else w.sym
  def indepOrDep(val):
    return w.dep if w.opt.klass in val else w.indep
  for col,val in enumerate(row):
    numOrSym(val).append(col)
    indepOrDep(val).append(col)
    w.name[col] = val
    w.index[val] = col

def indep(w,cols):
  for col in cols:
    if col in w.indep: yield col

def rows(file):
  def what(z):
    if the.TABLE.num in z: return float
    if the.TABLE.int in z: return int
    return noop
  def lines(): 
    n,kept = 0,""
    for line in open(file):
      now   = re.sub(w.bad,"",line)
      kept += now
      if kept:
        if not now[-1] == w.sep:
          yield n, map(atom, kept.split(w.sep))
          n += 1
          kept = "" 
  todo = None
  for n,line in lines():
    todo = todo or [col,what(name) for col,name 
                    in enumerate(line) 
                    if not w.skip in name]
    yield n,[ comp(line[col])
              for col,comp in todo ]
