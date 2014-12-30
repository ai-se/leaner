from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

"""

# Test Cases for COCOMO

"""
from cocomo import *

@go
def _range():
 for n in xrange(2):
    all= complete(flight)
    print("\n",n)
    for k,v in all.items():
      print("\t",k,v)


def sample(seed=1,n=1000,rx=doNothing,logAll=None,
           score=COCOMO2,what='effort',
           projects=[anything,flight,ground,osp,osp2],
           ):  
  rseed(seed)
  COL()
  the.COL.buffer=n
  logAll=logAll or N()
  logs= []
  for project in projects:
    log = N()
    logs += [log]
    log.name = project.__name__
    for _ in xrange(n):
      settings = complete(project, rx() or {})
      x = score(settings)
      log.tell(x)
      logAll.tell(x)
  for log in sorted(logs, key = lambda log: log.median()) :
    name = log.name
    kept = log.kept()
    mid = kept[int(len(kept)*0.5)]
    yield (mid,
           xtile(log.kept(),
                 lo=logAll.lo,
                 hi=logAll.hi,
                 chops=[0,0.25,0.5,0.75,0.999],
                 marks=["-"," "," ","-"," "],
                 width=30,
                 show= "%5d"),
            '%s(%s),' % (name,rx.__name__))

@go
def _coc(): 
  sample()
 

@go
def _stink(): 
  sample(score=badSmell,
         what="Bad smells")

@go
def _ospStinks(model=None,rx=None):
  rseed(1)
  for v,(x1,v1,x2,v2) in \
      whatStinks(model or osp, 
                 rx=rx or \
                         dict(cplx=[4],
                              rely=[1,2,3,5])):
    print('stink = %5s when' % v,
          x1,'=',v1,'and',x2,'=',v2)

 
@go
def _treat(n=1000):
 logAll=N()
 for m in [anything,flight,ground,osp,osp2]:
    print("")
    all = [] 
    for what,rx1 in rx().items():
        for one in sample(m,logAll=logAll, 
                     rx=rx1,projects=[m],
                      what='%s(%s)' % (m.__name__,what)):
            all += [one]
    for a,b,c in sorted(all):
      print(a,b,c)

_treat()    

"""
"*" not in right place
3345.84795964 (- *  -----     |              ),    4,  1367,  3345,  5771, 12018 anything(reduceFunctionality),
6177.82686741 (---    *   ----|-----------   ),    6,  2660,  6177, 10087, 24230 anything(improvePrecendentnessDevelopmentFlexibility),
6849.67132806 (--   *   ------|---           ),   11,  2682,  6849, 11512, 24972 anything(increaseArchitecturalAnalysisRiskResolution),
7051.03224069 (--   *   ------|------------- ),   17,  3111,  7051, 11976, 37848 anything(improvePersonnel),
7072.58607921 (--    *   -----|----------    ),   19,  3080,  7072, 11390, 29063 anything(improveProcessMaturity),
7239.65938544 (--    *   -----|------------- ),    7,  2869,  7239, 11924, 34058 anything(improveTeam),
7251.61545498 (--    *    ----|------------- ),    6,  2805,  7251, 12708, 32442 anything(reduceQuality),
7500.63196142 (--   *    -----|--------      ),    6,  3049,  7500, 13376, 31301 anything(relaxSchedule),
7831.11742136 (--    *   -----|------        ),   17,  3404,  7831, 13105, 28934 anything(improveToolsTechniquesPlatform),
8221.04571379 (--    *   -----|------------- ),    6,  3731,  8221, 13210, 37938 anything(doNothing),
"""

      
 