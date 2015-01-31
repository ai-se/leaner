class o:
  def d(i)           : return i.__dict__
  def update(i,**d)  : i.d().update(**d); return i
  def has(i,k)    : return k in i.d()
  def __init__(i,**d): i.update(**d)
  def __repr__(i)    :  
    def name(x):
      f = lambda x: x.__class__.__name__ == 'function'
      return x.__name__ if f(x) else x
    keys = [k for k in sorted(i.d().keys()) 
            if k[0] is not "_"]
    show = [':%s %s' % (k, name(i.d()[k])) 
            for k in keys]
    return '{'+' '.join(show)+'}'
    
class Counts(): # Add/delete counts of numbers.
    def __init__(i,inits=[]):
      i.zero()
      for number in inits: i + number 
    def zero(i): i.n = i.mu = i.m2 = 0.0
    def sd(i)  : 
      if i.n < 2: return i.mu
      else:       
        return (max(0,i.m2)*1.0/(i.n - 1))**0.5
    def __add__(i,x):
      i.n  += 1
      delta = x - i.mu
      i.mu += delta/(1.0*i.n)
      i.m2 += delta*(x - i.mu)
    def __sub__(i,x):
      if i.n < 2: return i.zero()
      i.n  -= 1
      delta = x - i.mu
      i.mu -= delta/(1.0*i.n)
      i.m2 -= delta*(x - i.mu)    

class Span:
    def __init__(i,x,lo,hi):
        i.x,i.lo,i.hi=x,lo,hi
        i.key=hash((x,lo,hi))
    def __hash__(i) : return i.key
    def __repr__(i) : return '%s <= %s <= %s' % (i.lo,i.x,i.hi)
        
class Range:
    def __init__(i,x=None,attr=None,y=None,rows=None):
        i.n     = len(rows)
        i.rows  = set(rows)
        i.attr  = attr
        i.x,i.y = x,y
        i.key   = Span(attr,x.lo,x.hi) 
    def __hash__(i): 
        return hash(i.key)
    def __repr__(i):
        return '%s:%s' % (i.key,i.n)
        
class Rule:
  def __init__(i,ranges,rows,score=lambda x:1):
    i.ranges=ranges
    i.keys=set(map(lambda z:z.key, ranges))
    i.rows=rows
    i.score=score
  def __repr__(i):
    return '%s:%s' % (str(map(str,i.ranges)),len(i.rows))
  def same(i,j):
    if len(i.keys) < len(j.keys):
      return j.same(i)
    else: # is the smaller a subset of the larger
      return j.keys.issubset(i.keys)
  def score(i):
    def most(j,n):  hi[j]=max(n, hi.get(j,-1*10**32))
    def least(j,n): lo[j]=min(n, hi.get(j,   10**32))
    def norm(j,n):  return (n - lo[j] ) / (hi[j] - lo[j] + 0.0001) 
    lo,hi = {}, {}
    for one in i.data:
      for j in i.less: least(j,one[j])
      for j in i.more: most(j, one[j])
    all,n=0,0
    for one in i.data:
      for j in i.less:
        n   += 1 
        all += (1 - norm(j,one[j]))**2
      for j in i.more:
        n   += 1 
        all += norm(j,one[j])**2
    return all**2 / n**2
  def __add__(i,j): 
   if i.same(j): 
     return False
   ranges = list(set(i.ranges + j.ranges)) # list uniques
   ranges = sorted(ranges,key=lambda x:x.attr) 
   b4  = ranges[0] 
   rows = b4.rows
   for now in ranges[1:]:
     if now.attr == b4.attr:
       rows = rows | now.rows
     else:
       rows = rows & now.rows 
     if not rows: 
       return False
     b4 = now
   return Rule(ranges,rows,i.score)
 
def g(lst,n=0):
  return map(lambda x:round(x,n),lst)

def data(**d):  
  names=d["names"]
  data=d["data"]
  more=[i for i,name in enumerate(names) if ">" in name]
  less=[i for i,name in enumerate(names) if "<" in name]
  dep = more+less
  indep=[i for i,name in enumerate(names) if not i in dep]
  return o(more=more,less=less,indep=indep,names=names,
           data=map(Row,data))
  
class Row:
  id=0
  def __init__(i,cells):
    i.cells= cells
    Row.id = i.id = Row.id+1
  def __hash__(i): return i.id
  def __getitem__(i, n): return i.cells[n]