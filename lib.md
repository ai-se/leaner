# lib

This file is part of LEANER where say that data mining is easy:

1. Find some crap;
2. Cut the crap;
3. Go to step 1.

Want to know more? 

+ Download [lib.py](https://github.com/ai-se/timm/blob/master/leaner/src/lib.py)
+ Read our [home](README.md) page.

____


# General stuff

````python
from config import *
import random
````

## Type stuff

````python
def ako(x,y): return isinstance(x,y)
````

## Random stuff

````python
r   = random.random
seed= random.seed
ask = random.choice

def shuffle(lst): random.shuffle(lst); return lst
````

## Iterator Stuff

````python
def pairs(lst):
  "Return all pairs of items i,i+1 from a list."
  last=lst[0]
  for i in lst[1:]:
    yield last,i
    last = i
````

## Stats stuff

````python
def cliffsDelta(lst1, lst2,dull=None):
  dull = dull or the.LIB.dull
  more = less = 0
  for x in lst1:
    for y in lst2:
      if x > y : more += 1
      if x < y : less += 1
  d = (more - less) / (len(lst1)*len(lst2))
  return abs(d) > dull
````

## Printing stuff

Print on or more of anything (no new lines).

````python
def say(*l):sys.stdout.write(', '.join(map(str,l))) 
````

Print list of numbers without too many decimal places.

````python
def g(lst,n=None):
  if n is None: n = the.LIB.points
  for col,val in enumerate(lst):
    if isinstance(val,float): val = round(val,n)
    lst[col] = val
  return lst
````

Print a list of lists, aligning all the columns.

````python
def printm(matrix):
  s = [[str(e) for e in row] for row in matrix]
  lens = [max(map(len, col)) for col in zip(*s)]
  fmt = ' | '.join('{{:{}}}'.format(x) for x in lens)
  for row in [fmt.format(*row) for row in s]:
    print(row)
````

Print a list of numbers (possibly
unsorted) 
 and presents them as a horizontal
 percentile chart (in ascii format). The default is a 
  contracted _quintile_ that shows the 
  10,30,50,70,90 breaks in the data (but this can be 
  changed- see the optional flags of the function)

````python
def xtile(lst,lo=0,hi=100,width=50,
             chops=[0.1 ,0.3,0.5,0.7,0.9],
             marks=["-" ," "," ","-"," "],
             bar="|",star="*",show=" %3.0f"):
  def pos(p)   : return ordered[int(len(lst)*p)]
  def place(x) : 
    return int(width*float((x - lo))/(hi-lo+0.001))
  def pretty(lst) : 
    return ', '.join([show % x for x in lst])
  ordered = sorted(lst)
  lo      = min(lo,ordered[0])
  hi      = max(hi,ordered[-1])
  what    = [pos(p)   for p in chops]
  where   = [place(n) for n in  what]
  out     = [" "] * width
  for one,two in pairs(where):
    for i in range(one,two): 
      out[i] = marks[0]
    marks = marks[1:]
  out[int(width/2)]    = bar
  out[place(pos(0.5))] = star 
  return '('+''.join(out) +  ")," +  pretty(what)
````
