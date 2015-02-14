from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True
 
class Model:
    def __init__(i):
      i.flows,i.stocks,i.flows=[],[],[]
    def has(i,**d):
      for name, init in d.items(): ### XXX need a way to inclide zeros, hi, lo
        s=Stock(name,init,g=i) 
      
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

class Stocks:
  def __init__(i,x): i.contents = [x]
  def __plus__(i,x): i.contents += [x]
  
class Part:
  def __init__(i):
      i.parts=[]

class Stock:
  id=0
  nodes={}
  def __init__(i,name,zero=0,lo=0,hi=10**32,g=None):
    Stock.id = i.id = Stock.id + 1
    i.g=g
    i.name,i.lo,i.hi,i.zero = name,lo,hi,zero
    Stock.nodes[i.id] = i
  def __repr__(i)  : return 'Stock(%s)' % i.name
  def __mul__(i,n) : return (i,n)
  def __rmul__(i,z): return i.__mul__(z)
  def __iadd__(i,(obj,rate)):
    Flow(src=obj,sink=i,rate=rate)
    return i
  def __isub__(i,(obj,rate)): 
    Flow(sink=obj,src=i,rate=rate)
    return i

S = Stock

def stocks(**d):
  return [S(k,v) for k,v in d.items()]
  
a,b,c=stocks(a=10, b=20, c=30)

a += 3*b
a -= 2*c

print(Flow.flows)

def run(steps=10):
  b4 = {}
  for v in Stock.nodes.values():
    print(v)
    b4[v.id] = v.zero
  for step in xrange(steps):
    print("")
    now = {id:b4[id] for id in b4}
    for flow in Flow.flows: flow.step(b4,now)
    for v in Stock.nodes.values():
      now[v.id] = max(min(v.hi,now[v.id]),v.lo)
    for k in now: print(Stock.nodes[k],now[k])
    b4  = now
  return b4

print(run())

