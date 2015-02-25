from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True
"""

# Lib

## Demo-able

A code file X.py may have an associated file Xeg.py
containing examples, demo, litle tutorials on how to use X.py.
If functions in Xeg.py are decorated with  `@go`, then
those functions will run just as a side-effect of loading that code. 
And if those functions print True and False then you can generate the world's
smallest test suite just by counting the percent True and Falses

"""
def go(f,ignoreErrors=True):
  doc= '# '+f.__doc__+"\n" if f.__doc__ else ""
  s='|'+'='*40 +'\n'
  print('\n==|',f.func_name + ' ' + s+doc)
  f()
  return f
"""

## Misc Utilities

### The Container Idiom

Just a place to store and update named slots.
When printed, any slot starting with "_"
is not shown. Any slot that is a function
name is displayed using it's function name.

"""
class o:
  def __init__(i,**d) : i.add(**d)
  def has(i): return i.__dict__
  def add(i,**d) : i.has().update(**d); return i
  def __setitem__(i,k,v): i.has()[k] = v
  def __repr__(i) :
    f = lambda z: z.__class__.__name__ == 'function'
    name   = lambda z: z.__name__ if f(z) else z
    public = lambda z: not "_" is z[0]
    d    = i.has()
    show = [':%s=%s' % (k,name(d[k])) 
            for k in sorted(d.keys()) if public(k)]
    return '{'+' '.join(show)+'}'
"""

## The Settings Idiom

+ All  settings are stored in some global space so 
     + Optimizers have one place to go to adjust settings;
     + We have one place to go and print the options;
+ These settings can be set from multiple places all over the code
  using  a function decorated with "_@setting_".

"""
the=o()

def setting(f):
  def wrapper(**d):
    tmp = the[f.__name__] = f().add(**d)
    return tmp
  wrapper()
  return wrapper
"""

For example, my code can now contain functions decorated by @setting
and all their values can be accessed via (e.g.) `the.GENIC.k`'or updated 
via (e.g.) `GENIC(k=100)`. MOre workds
"""

class settings(object):
  def __init__(i, what,**args):
     i.what,i.args=what,args
  def __enter__(i):
     return i.what(**i.args)
  def __exit__(i,*ignore):
    i.what()

"""
## Misc stuff

### Random Stuff 

"""
import random
r     = random.random
rseed = random.seed

def shuffle(lst): random.shuffle(lst); return lst

def noop(z)  : return z
def first(z) : return z[0]
def second(z): return z[1]
def third(z) : return z[2]
def last(z)  : return z[-1]

def ntiles(lst,tiles):
  thing = lambda z: lst[ int(len(lst)*z)  ]
  return [ thing(tile) for tile in tiles ]
"""

### Print Stuff

`Say` prints without new lines.

"""
def say(*lst): print(', '.join(map(str,lst)),end="")
"""

`G` prints long numbers with just a few decimal places.
 
"""
import math
pi  = math.pi
sqrt  =math.sqrt

def normpdf(mean, sd, x):
    var = sd**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(x-mean)**2/(2*var))
    return num/denom

  
def g(lst,n=3):
  for col,val in enumerate(lst):
    if isinstance(val,float): val = round(val,n)
    lst[col] = val
  return lst

def runs(lst):
  for j,two in enumerate(lst):
    if j == 0:
      one,i = two,0
    if one!=two:
      yield j - i,one
      i = j
    one=two
  yield j - i + 1,two
"""

`Printm` prings a list of lists, aligning each column.

"""
def printm(matrix,underline=None):
  if underline:
    matrix = [ matrix[0]]+ [
              [("-"*len(s)) for s in matrix[0]]
             ] +  matrix[1:]
  s = [[str(e) for e in row] for row in matrix]
  lens = [max(map(len, col)) for col in zip(*s)]
  fmt = ' | '.join('{{:{}}}'.format(x) for x in lens)
  for row in [fmt.format(*row) for row in s]:
    print(row)

def median(lst):
  "Assumes lst is ordered."
  n   = len(lst)
  a   = int(0.25 * n)  
  b1  = int(0.50 * n) ; b2 = max(b1 - 1,0)
  c   = int(0.75 * n)
  iqr = lst[c] - lst[a]
  mid = lst[b1] if n % 2 else ((lst[b1] + lst[b2]) / 2) 
  return mid, iqr

