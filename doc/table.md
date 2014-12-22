
<small>_This file is part of LEANER. To know more, view the source code [table.py](../src/table.py) or read our [home](https://github.com/ai-se/leaner) page._</small>



# Handling Tables of Data

A table is a set of rows and  a header
storing information about each column,

Column headers are either `N` nums or `S`
symbols objects. Columns are divided
into independent and dependent variables.

+ Dependent symbolic columns are called `klasses`;
+ Dependent numeric columns can be optionally
  tagged with a boolean `like` (and we want more
   things with
  `like==True`).

````python
from cols import *
import zipfile,re,fnmatch

@setting
def TBL(**d): return o(
    # Thresholds are from http://goo.gl/25bAh9
    skip="?",
    num="$",
    sep  = ',',
    bad = r'(["\' \t\r\n]|#.*)',
    datafile = lambda z: '../data/%s' %z
  ).update(**d)

def table(**d):
  return o(indep=[], dep=[],rows=[]
           ).update(**d)

def unzip(zipped, want):
  with zipfile.ZipFile(zipped,'r') as archive:
    for got in archive.namelist():
      if fnmatch.fnmatch(got, want):
        for line in archive.open(got,'r'):
          yield line
        break

def rows(file, source=open):
  w = the.TBL
  def reader(name):
    return float if w.num in name else identity
  def lines(): 
    n,kept = 0,""
    for line in source(file):
      now   = re.sub(w.bad,"",line)
      kept += now
      if kept:
        if not now[-1] == w.sep:
          yield n, kept.split(w.sep)
          n += 1
          kept = "" 
  todo = None
  for n,line in lines():
    if n == 0:
      todo = [(n,reader(header))
              for n,header in enumerate(line)
              if not w.skip in header]
    else:
      yield n, [ read(line[col]) 
                 for col,read in todo ]

````
