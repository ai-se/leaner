from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

#  _____ _   _           _             
# /  ___| | (_)         (_)            
# \ `--.| |_ _ _ __ _ __ _ _ __   __ _ 
#  `--. \ __| | '__| '__| | '_ \ / _` |
# /\__/ / |_| | |  | |  | | | | | (_| |
# \____/ \__|_|_|  |_|  |_|_| |_|\__, |
#                                 __/ |
#                                |___/ 
# ______                               
# | ___ \                              
# | |_/ /_ _ _ __   ___ _ __ ___       
# |  __/ _` | '_ \ / _ \ '__/ __|      
# | | | (_| | |_) |  __/ |  \__ \       
# \_|  \__,_| .__/ \___|_|  |___/      
#           | |                        
#           |_|                        
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

"""

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
    tmp = the[f.__name__] = f(**d)
    return tmp
  wrapper()
  return wrapper
"""

For example, my code can now contain functions decorated by @setting
and all their values can be accessed via (e.g.) `the.GENIC.k`'or updated 
via (e.g.) `GENIC(k=100)`.

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
"""

### Print Stuff

`Say` prints without new lines.

"""
def say(*lst): print(', '.join(map(str,lst)),end="")
"""

`G` prints long numbers with just a few decimal places.
 
"""
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
