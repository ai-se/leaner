
<small>_This file is part of LEANER. To know more, view the source code [columneg.py](../src/columneg.py) or read our [home](https://github.com/ai-se/leaner) page._</small>



# Column stuff (demos)

````python
from column import *

@go
def _S():
  s=S(list('from __future__ import division'))
  print(s.all,s.ent(),s.ask())
  l1 = s.likely('i')
  l2 = s.likely('f')
  print('rare less likely:',l2< l1)

@go
def _N():
  rseed(1)
  n=N([x for x in xrange(100)])
  print(n.mu==49.5,n.sd(), n.lo==0,n.hi==99)
  l1=n.likely(49)
  l2=n.likely(1)
  print("good 49 likely:", round(l1,5)==0.01375)
  print("good 1 likely:" , round(l2,5)==0.00340)
  print('outlier less likely:',l1,l2,l2< l1)
  
````
