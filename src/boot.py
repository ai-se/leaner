from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

"""
# Boot Code

Code needed before we can do anything else.

"""

def name(x):
  f = lambda x: x.__class__.__name__ == 'function'
  return x.__name__ if f(x) else x

class o:
  def d(i)           : return i.__dict__
  def update(i,**d)  : i.d().update(**d); return i
  def __init__(i,**d): i.update(**d)
  def __repr__(i)    :  
    keys = [k for k in sorted(i.d().keys()) 
            if k[0] is not "_"]
    show = [':%s %s' % (k, name(i.d()[k])) 
            for k in keys]
    return '{'+' '.join(show)+'}'

the=o()

def setting(f):
  def wrapper(**d):
    tmp = the.d()[f.__name__] = f(**d)
    return tmp
  wrapper()
  return wrapper

