from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

"""

# Test Cases for COCOMO

"""

from cocomo import *

#@go
def _range():
 for n in xrange(2):
    all,_ = complete(flight)
    print("\n",n)
    for k,v in all.items():
      print("\t",k,v)


def sample(seed=1,n=1000,score=COCOMO2,what='effort'):  
  rseed(seed)
  projects=[anything,flight,ground,osp,osp2]
  COL()
  the.COL.buffer=n
  logAll=N()
  logs= {} 
  for project in projects:
    log = logs[project.__name__] = N()
    for _ in xrange(n):
      settings, _ = complete(project)
      x = score(settings)
      log.tell(x)
      logAll.tell(x)
  print("\n\n---|",what,"|---------------\n")
  for project in projects:
    name = project.__name__
    log = logs[name]
    print ('%9s,' % name,
           xtile(log.kept(),
                 lo=logAll.lo,
                 hi=logAll.hi,
                 chops=[0,0.25,0.5,0.75,0.999],
                 marks=["-"," "," ","-"," "],
                 width=30,
                 show= "%5d"))

#@go
def _coc(): 
  sample()

#@go
def _stink(): 
  sample(score=badSmell,
         what="Bad smells")

#@go
def _ospStinks():
  rseed(1)
  for v,(x1,v1,x2,v2) in whatStinks(osp):
    print('stink = %.2f when' % v,x1,'=',v1,'and',x2,'=',v2)

#@go
def _run1():
  print(run1(osp))

def _run():   
   for m in [flight]: #osp,osp2,flight,ground]:
      rseed(1)
      run(m)

def _de():
    for m in [flight,osp,osp2,ground,anything]:
      rseed(1)
      print("\n",m.__name__)
      des(m)
      
_de()