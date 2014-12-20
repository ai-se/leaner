# boot

This file is part of LEANER where say that data mining is easy:

1. Find some crap;
2. Cut the crap;
3. Go to step 1.

Want to know more? 

+ Download [boot.py](https://github.com/ai-se/timm/blob/master/leaner/src/boot.py)
+ Read our [home](README.md) page.

____

# Boot code: stuff needed before anything else

## `o`: a Generic Holder for Names Slots

Useful when you want a bag of names things, that 
do not need methods.

````python
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

def name(x):
  f = lambda x: x.__class__.__name__ == 'function'
  return x.__name__ if f(x) else x
````

## `setting`: a Wrapper that Remembers the Settings

````python
def setting(f):
  def wrapper(**d):
    tmp = the.d()[f.__name__] = f(**d)
    return tmp
  wrapper()
  return wrapper
````

## 'the`: Where we Store the Globals

````python
the=o()
````

Use the following to print the global settings

````python
def THAT(x=the,s="",pre=""):
  d = x.d()
  say(pre)
  for k in sorted(d.keys()):
    if k[0] is not "_":
      say(s + (':%s ' % k))
      y = d[k]
      THAT(y,s+"   ","\n") if ako(y,o) else print(y)
````
