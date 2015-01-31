from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

import housing,ranges
from rangesLib import *

# add in scorerd. abcd mre, lift

def g(x): return ('%g' % x)

def _rangeLib():
  def show(n,rule):
    print(n,rule)
    print(n,sorted(map(lambda z:z.id,rule.rows)))  
  t=housing.housing() 
  b4=Counts(map(lambda l:l[-1],t.data))
  r=[]
  for i  in t.indep:
    r=ranges.sdiv(t.data,attr=t.names[i],tiny=20,
              x=lambda z:z[i],cuts=r)
  #exit()
  r = sorted(r,key=lambda z :z.y.mu*-1)
  for one in r:
    if one.y.mu > (b4.mu + b4.sd()): 
      print(one.attr, 
        one.x.lo, one.x.hi,g(one.y.mu),g(one.y.sd),g(b4.mu),g(b4.sd()),sep=",")
  #exit()      
  for _ in range(20):
      print("")
      row1  = random.choice(r)
      row2  = random.choice(r)
      rule1 = Rule([row1],row1.rows)
      rule2 = Rule([row2],row2.rows)
      show(1,rule1)
      show(2,rule2)
      rule3 = rule1+rule2
      if rule3:
        show(3,rule3)
      
if __name__ == "__main__":
    _rangeLib()