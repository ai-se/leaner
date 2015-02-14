from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True
 
class Model:
  def __init__(i):
    i.nflows = i.nstocks = 0
    i.flows,i.stocks,i.aux= [],{},{}
    i.spec()
  def spec(i): pass
  def one(i,x,init):
    tmp = i.stocks[x] = i.stocks[x] \
            if x in i.stocks else Stock(x,i,init)
    return tmp
  def has(i,**d):
    return [i.one(one,x,init)
            for x, init in d.items()]

class Flow:
  def __init__(i,model,src=None,sink=None,rate=1,times=None):
    i.model = model
    i.src, i.sink, i.rate,i.times = src,sink,rate,times
    i.model.flows += [i]
  def step(i,b4,now):
    delta = i.rate
    if i.times:
      delta *= b4[i.times.id] 
    gap   = i.sink.hi - now[i.sink.id]
    delta = min(delta, gap, now[i.src.id])
    now[i.src.id ] = b4[i.src.id ] - amount
    now[i.sink.id] = b4[i.sink.id] + amount
  def __repr__(i):
    return '%s ==> %s * %s' % (i.src,i.sink,i.rate)

class Stock:
  def __init__(i,name,model,zero,lo=0,hi=10**32):
    model.nstocks =  i.id = model.nstocks + 1
    i.model = model
    i.name,i.lo,i.hi,i.zero = name,lo,hi,zero
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

class Model1(Model):
  def spec(i):
    a,b,c = i.has(a=10, b=20, c=30)
    a += 3*b
    a -= 2*c 

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

