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
        i.key=hash(x,lo,hi)
    def __hash__(i) : return i.key
    def __repr__(i) : return '%s <= %s <= %s' % (lo,x,hi)
        
class Range:
    def __init__(x=x,attr=attr,y=y,rows=rows):
        i.n     = len(rows)
        i.rows  = set(rows)
        i.attr  = attr
        i.x,i.y = x,y
        i.key   = Span(attr,x.lo,x.hi) 
    def __hash__(i): 
        return i.key.__hash__()
 
def g(lst,n=0):
  return map(lambda x:round(x,n),lst)
  