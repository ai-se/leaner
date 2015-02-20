from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

#  __                              __
# / _\_   _ _ __  _ __   ___  _ __| |_     
# \ \| | | | '_ \| '_ \ / _ \| '__| __|    
# _\ \ |_| | |_) | |_) | (_) | |  | |_     
# \__/\__,_| .__/| .__/ \___/|_|   \__|    
#          |_|   |_|                       
#    ___                                   
#   /___\_ __   ___ _ __                   
#  //  // '_ \ / _ \ '_ \                  
# / \_//| |_) |  __/ | | |                 
# \___/ | .__/ \___|_| |_|                 
#       |_|                                
#  __        __ _                          
# / _\ ___  / _| |___      ____ _ _ __ ___ 
# \ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \
# _\ \ (_) |  _| |_ \ V  V / (_| | | |  __/
# \__/\___/|_|  \__| \_/\_/ \__,_|_|  \___|
                                         
#  __      _            _   _     _        
# / _\ ___(_) ___ _ __ | |_(_)___| |_      
# \ \ / __| |/ _ \ '_ \| __| / __| __|     
# _\ \ (__| |  __/ | | | |_| \__ \ |_      
# \__/\___|_|\___|_| |_|\__|_|___/\__|            
#     
#
# Copyright (c) 2015, Tim Menzies, tim.menzies@gmail.com
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""# Lib.py

This file defines basic conventions and low-level
code to support "open software science" (OpeSS).

An open software scientist analyzes and shares
software artifacts with the goal of generating
libraries of trusted software tools.  Their
conclusions are repeatable, improvable and
refutable.

Tools, not just opions..

Open software scientists use literature
programming. Their code comments describe
experiments (simulation, data mining, etc) that
execute within their code.  That code does not just
run, it reports opinions.  It comments on whether X
is better than Y.

To encourage sharing and an open analysis of all concluions,
OpeSS uses open source tools. All work is stored on-line
in repositories that support commenting, forking, and merging.

The world we live in today is much more a man-made,
or artificial, world than it is a natural
world. Almost every element in our environment shows
evidence of human artifice.

Because of its abstract character and its symbol
manipulating generality, the digital computer has
greatly extended the range of systems whose behavior
can be imitated. Generally we now call the imitation
"simulation," and we try to understand the imitated
system by testing the simulation in a variety of
simulated, or imitated, environments.  Artificial
systems and adaptive systems have properties that
make them particularly susceptible to simulation via
simplified models.

A frequently asked question is how can a simulation
ever tell us anything that we do not already know?
The obvious point is that, even when we have correct
premises, it may be very difficult to discover what
they imply. All correct reasoning is a grand system
of tautologies, but only God can make direct use of
that fact. The rest of us must painstakingly and
fallibly tease out the consequences of our
assumptions.

In science and engineering the study of
"systems" is an increasingly popular
activity. Its popularity is more a
response to a pressing need for
synthesizing and analyzing complexity
than it is to any large development of a
body of knowledge and technique for
dealing with complexity. If this
popularity is to be more than a fad,
necessity will have to mother invention
and provide substance to go with the
name.


## Principles

### Shareable

+ Code starts with some open source license statement.
+ Code stored in some downloadable public space (e.g. Github).
+ Coded in some widely used language (e.g. Python) with extensive 
  on-line tutorialsl e.g. [Stackoverflow.com](http://stackoverflow.com/questions/tagged/python).

### Readable

#### Succinct

Not arcane, but lots of little short and useful code snippets. 

#### Abstract

Heavy use of abstraction to simplify processing of low-level details.

#### Succinct

Deliver features, not code. N-1 lines of code better than N. Write your code then cut it in half. YAGNI! YAGNI!

#### Functional more Object-Oriented

_(BEGIN PERSONNEL BIAS)_

N-1 classes better than N. Give us this day our daily lambda. 

Why? Well functional programemers can define and code a dozen useful patterns in the time it
takes a pure-OO guy to code one class.

#### Commented

Comments tell a story. Describe each function in terms
of some idiom (small thing) or pattern (larger thing)
describing something that someone else other than
the programmer might actually care about

Code written to be included into a two column paper:

+ All comments written in multiline strings and in 
  Pandoc style markdown.
      + File contains only one H1 header.
+ No line longer than 52 characters.  Which means
  for a language like Python:
    + _Self_ replaced with "_i_".
    + Indented with two characters.

### Sensible

Using Python 2.7 (cause of compatability issues).
Adopt the future `print` and `division`
functions. Do not write spurious _.pyc_ files.
For examples of the use of these idioms, see top of this file.

### Demo-able

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
  if ignoreErrors:
    try:
      f()
    except:
      print('Demo function',f,' did not crash: False')
  else: f()
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
  def add(i,**d) : i.__dict__.update(**d); return i
  def __repr__(i) :
    f = lambda z: z.__class__.__name__ == 'function'
    name   = lambda z: z.__name__ if f(z) else z
    public = lambda z: not "_" is z[0]
    d    = i.__dict__
    show = [':%s=%s' % (k,name(d[k])) 
            for k in sorted(d.keys()) if public[k]]
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
    tmp = the[f.__name__] = f(**d)
    return tmp
  return wrapper
"""

For example, my code can now contain functions decorated by @setting
and all their values can be accessed via (e.g.) `the.GENIC.k`'or updated 
via (e.g.) `GENIC(k=100)`.

"""
@setting
def GENIC(**d): 
  def halfEraDivK(z): 
    return z.opt.era/z.opt.k/2
  return o(
    k     = 10,
    era   = 1000,
    buffer= 500,
    tiny  = halfEraDivK,
    seed  = 1).add(**d)

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
"""

## Misc stuff

### Random Stuff 

"""
import random
rand= random.random
rseed= random.seed

def shuffle(lst): random.shuffle(lst); return lst

def noop(x): return x
"""

### Print Stuff

`Say` prints without new lines.

"""
def say(**lst): print(', '.join(map(str,lst)),end="")
"""

`G` prints long numbers with just a few decimal places.
 
"""
def g(lst,n=3):
  for col,val in enumerate(lst):
    if isinstance(val,float): val = round(val,n)
    lst[col] = val
  return lst
"""

`Printm` prings a list of lists, aligning each column.

"""
def printm(matrix):
  s = [[str(e) for e in row] for row in matrix]
  lens = [max(map(len, col)) for col in zip(*s)]
  fmt = ' | '.join('{{:{}}}'.format(x) for x in lens)
  for row in [fmt.format(*row) for row in s]:
    print(row)


import math

class S(): 
  def __init__(i,inits=[]):
    i.n,i.count,i._also = 0, {}, None
    for number in inits: i += number 
  def __iadd__(i,z): return i.inc(z,  1)
  def __isub__(i,z): return i.inc(z, -1)
  def inc(i,z):
    i._also = None
    i.n += n
    i.counts[z] = i.counts.get(z,0) + n
    return i
  def most(i): return i.also().most
  def mode(i): return i.also().mode
  def ent(i) : return i.also().e
  def also():
    if not i._also:
      e,most.mode = 0,0,None
      for z in i.counts:
        if i.counts[z] > most:
          most,mode = i.counts[z],z
        p = i.counts[z]/i.n
        if p: 
          e -= p*math.log(p,2)
        i._also = o(most=most,mode=mode,e=e)
    return i._also
  
class N(): 
  def __init__(i,inits=[]):
    i.n = i.mu = i.m2 = i.sd = 0
    for number in inits: i += number 
  def _sd(i)  :
    if i.n > 1 :
      i.sd = (max(0,i.m2)*1.0/(i.n - 1))**0.5
    return i
  def __iadd__(i,x):
    i.n  += 1
    delta = x - i.mu
    i.mu += delta/(1.0*i.n)
    i.m2 += delta*(x - i.mu)
    return i._also()
  def __isub__(i,x):
    i.n  -= 1
    delta = x - i.mu
    i.mu -= delta/(1.0*i.n)
    i.m2 -= delta*(x - i.mu)
    return i._also()
  
  
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

def fuse(w,new,n):
  u0,u,dob,old = w.centroids[n]
  u1 = 1
  out = [None]*len(old)
  for col in w.sym:
    x0,x1 = old[col], new[col]
    out[col] = x1 if rand() < 1/(u0+u1) else x0
  for col in w.num:
    x0,x1= old[col], new[col]
    out[col] = (u0*x0 + u1*x1)/ (u0+u1)
  w.centroids[n] = (u0 + u1,u+u1, dob, out)

def more(w,n,row):
  w.centroids += [(1,1,n,row)]


def less(w,n) :
  b4 = len(w.centroids)
  w.centroids = [(1,u,dob,row) 
                 for u0,u,dob,row in w.centroids 
                 if u0 > w.opt.tiny(w)]
  print("at n=%s, pruning %s%% of clusters" % (
         n,  int(100*(b4 - len(w.centroids))/b4)))

def nearest(w,row):
  def norm(val,col):
    lo, hi = w.min[col], w.max[col]
    return (val - lo ) / (hi - lo + 0.00001)
  def dist(centroid):
    n,d = 0,0
    for col in indep(w, w.num):
      x1,x2 = row[col], centroid[col]
      n1,n2 = norm(x1,col), norm(x2,col)
      d    += (n1 - n2)**2
      n    += 1
    for col in indep(w, w.sym):
      x1,x2 = row[col],centroid[col]
      d    += (0 if x1 == x2 else 1)
      n    += 1
    return d**0.5 / n**0.5
  lo, out = 10**32, None
  for n,(_,_,_,centroid) in enumerate(w.centroids):
    d = dist(centroid)
    if d < lo:
      lo,out = d,n
  return out

def report(w,clusters):
  cols = w.index.keys()
  header = sorted(w.name.keys())
  header= [w.name[i] for i in header]
  matrix = [['gen','caughtLast',
              'caughtAll','dob'] + header]
  caught=0
  for m,(u0,u,dob,centroid) in enumerate(clusters):
    if u0 > w.opt.tiny(w):
      caught += u0
      matrix += [[m+1,u0,u,dob] + g(centroid,2)]
  print("\ncaught in last gen =%s%%\n" %
        int(100*caught/w.opt.era))
  printm(matrix)
  options = cached()
  for x in options: print(x,options[x])
  print("")

def genic(src='data/diabetes.csv',opt=None):
  w = o(num=[], sym=[], dep=[], indep=[],
        centroids=[],
        min={}, max={}, name={},index={},
        opt=opt or genic0())
  for n, row in table(src,w):
    data(w,row)
    if len(w.centroids) < w.opt.k:
      more(w,n,row)
    else:
      fuse(w,row,nearest(w,row))
      if not (n % w.opt.era):
        less(w,n)
  return w,sorted(w.centroids,reverse=True)

def _genic( src='data/diabetes.csv'):
  if len(sys.argv) == 2:
    src= sys.argv[1]
  opt=genic0(k=8)
  seed(opt.seed)
  report(*genic(src,opt)) 

if __name__ == '__main__': _genic()

"""
data/diabetes2.csv (1.5M records).
caught in last gen =77%

gen | caughtLast | caughtAll | dob     | $preg | $plas  | $pres | $skin | $insu  | $mass | $pedi | $age  | =class        
1   | 205        | 390       | 1571001 | 2.04  | 97.08  | 65.03 | 23.25 | 52.6   | 29.19 | 0.35  | 24.14 | testednegative
2   | 146        | 2408      | 1560001 | 3.77  | 117.73 | 74.08 | 0.79  | 3.86   | 31.04 | 0.4   | 31.84 | testedpositive
3   | 119        | 824       | 1566001 | 7.54  | 142.17 | 78.47 | 7.53  | 16.58  | 29.72 | 0.46  | 52.1  | testednegative
4   | 109        | 252       | 1571002 | 2.39  | 145.63 | 73.09 | 30.13 | 201.47 | 34.58 | 0.35  | 28.57 | testednegative
5   | 106        | 2690      | 1554001 | 8.03  | 106.6  | 76.56 | 32.07 | 64.18  | 34.63 | 0.41  | 40.84 | testednegative
6   | 85         | 654       | 1569002 | 1.62  | 118.5  | 70.76 | 33.44 | 119.23 | 36.16 | 0.93  | 26.23 | testedpositive
genic0 {:buffer=500 :era=1000 :k=8 :klass== :num=$ :seed=1 :tiny=halfEraDivK}
rows0 {:bad=(["\' \t\r\n]|#.*) :sep=, :skip=?}

real	3m25.949s
user	3m7.403s
sys	0m2.315s
"""
