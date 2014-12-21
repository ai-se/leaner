
<small>_This file is part of LEANER. To know more, download [cols.py](https://github.com/ai-se/leaner/blob/master/src/cols.py)'s source or read our [home](https://github.com/ai-se/leaner) page._</small>


# Defining columns

````python
from lib import *
````

### `Col`: Generic Columns

````python
class Col:
  def tell(i,x):
    if x is None or x == the.COL.missing:
      return x
    i.n += 1
    i.tell1(i,x)
    return x
````

## `N`: Columns of Numbers

````python
class N(Col):
  def __init__(i,init=[],lo=None,hi=None,name=''):
    i.n, i.lo, i.hi, i.name = 0,lo,hi,str(name)
    i._kept = [None]*the.COL.buffer
    i.mu = i.m2= 0
    map(i.tell,init)
  def ask(i)     : return i.lo + r()*(i.hi - i.lo)
  def dist(i,x,y): return i.norm(x) - i.norm(y)
  def logger(i): 
    return N(name=i.name,lo=i.lo,hi=i.hi)
  def tell1(i,x):
    if i.lo is None: i.lo = x
    if i.hi is None: i.hi = x
    i.lo, i.hi = min(i.lo,x), max(i.hi,x)
    delta = x - i.mu
    i.mu += delta/i.n
    i.m2 += delta*(x - i.mu)
    l = len(i._kept)
    if r() <= l/i.n: i._kept[ int(r()*l) ]= x
  def sd(i):
    if i.n < 2: return 0
    return (max(0,i.m2)/(i.n - 1))**0.5
  def kept(i): 
    return [x for x in i._kept if x is not None]
  def norm(i,x):
    tmp =(x - i.lo) / (i.hi - i.lo + 0.00001)
    return max(0,min(tmp,1))
  def __repr__(i): 
    return '{:%s #%s [%s .. %s]}'%(
      i.name,i.n,i.lo ,i.hi)
  def likely(i,x,prior):
    return normpdf(x,i.mu.i.sd())
````

## `S`: Columns of Symbols

````python
class S(Col): 
  def __init__(i,all=None,name=''): 
    i.all = all or {}
    i.n = 0
    i.name = str(name)
  def tell1(i,x)  : 
    i.all[x] = i.all.get(x,0) + 1
  def ask(i)     : return(ask(i.all.keys()))
  def dist(i,x,y): return 0 if x==y else 1
  def norm(i,x)  : return x
  def logger(i)  : return S(name=i.name)
  def likely(i,x,prior):
    m = the.COL.m
    old = (i.all.get(x,0) + m*prior)/(i.n + m)
    
````
