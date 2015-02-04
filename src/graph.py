from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

class Flow:
  flows=[]
  def __init__(i,src=None,sink=None,rate=1,times=None):
    i.src, i.sink, i.rate,i.times = src,sink,rate,times
    Flow.flows += [i]
  def step(i,b4,now):
    amount = i.rate
    if i.times:
      amount *= b4[i.times.id]
    amount = min(amount,now[i.src.id])
    now[i.src.id ] = b4[i.src.id ] - amount
    now[i.sink.id] = b4[i.sink.id] + amount
  def __repr__(i):
    return '%s ==> %s * %s' % (i.src,i.sink,i.rate)
    
class V:
  id=0
  nodes={}
  def __init__(i,name,zero=0,lo=0,hi=10**32):
    V.id = i.id = V.id + 1
    i.name,i.lo,i.hi,i.zero = name,lo,hi,zero
    V.nodes[i.id] = i
  def __repr__(i): return 'Tub(%s)' % i.name
  def __mul__(i,n): return (i,n)
  def __iadd__(i,(obj,rate)):
    Flow(src=obj,sink=i,rate=rate)
    return i
  def __isub__(i,(obj,rate)): 
    Flow(sink=obj,src=i,rate=rate)
    return i
    
a,b,c=V("a",10),V("b",20),V("c",30)

a += b*3
a -= c*2
print(Flow.flows)

def run(steps=10):
  b4 = {}
  for v in V.nodes.values():
    print(v)
    b4[v.id] = v.zero
  for step in xrange(steps):
    print("")
    now = {id:b4[id] for id in b4}
    for flow in Flow.flows: flow.step(b4,now)
    for v in V.nodes.values():
      now[v.id] = max(min(v.hi,now[v.id]),v.lo)
    for k in now: print(V.nodes[k],now[k])
    b4  = now
  return b4

print(run())