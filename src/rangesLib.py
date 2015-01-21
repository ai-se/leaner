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

class Row:
  id=-1
  def __init__(i,cells):
    Row.id = i._id = Row.id + 1
    i.cells=cells
  def __getitem__(i,n): return i.cells[n]
  def __setitem__(i,n,x): i.cells[n] = x; return x
  def __hash__(i) : return i._id
  def __repr__(i):
    return 'Row'+str(i.cells)

class Range:
  def __init__(items,attr,val=lambda x:x[0]):
    ordered = sorted([Row[x] for x in list(items)],
                     key=lambda x:val(x))
    i.lo = val(ordered[0])
    i.hi = val(ordered[-1])
    i.items = set(ordered)
    i.attr, i.val = attr,val
  def __plus__(i,j):
    if i.attr==j.attr:
      return Range(set(i.items) | set(j.items),i.attr,i.val)
    else:
      return Range(set(i.items) & set(j.items),i.attr,i.val)
  def __repr__(i):
    return '%s=[%s..%s]' % (i.attr.i.lo,i.hi)


def g(lst,n=0):
  return map(lambda x:round(x,n),lst)
  