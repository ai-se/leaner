
## The Era Pattern

Run over the data using a window of size _era_.  For
each era, shuffle the data order. Return one row at
a time. Flag if this is the first row. Return 
at least _want_ number of rows.

````python
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
````

## The Table Pattern

The first row contains header info. All other rows are data.
Yield all rows, after updating header and row data information.

````python
def table0():
  return o(num=[],sym=[],ord=[],spec=[],
           more=[],less=[],klass=[],
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
  return t
````
