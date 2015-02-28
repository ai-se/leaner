from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from table import *
from abcd  import *

@setting
def NB(**d): 
  return o(
    m = 2,
    k = 1
  ).add(**d)

def ilearn(src, test, train):
  logs = {}
  for t,rows,era in eras(src):
    logs[era] = Abcd()
    for row in rows:
      k = theKlass(t,row)
      if era > 0:
        predicted = test(t,row)
        logs[era](k, predicted)
        logs[0](  k, predicted)
      train(t,row,k)
  return t,logs

def nb(f):
  klasses = {}
  def train(t,row,k):
    if not k in klasses:
      klasses[k] = header(t.spec)
    Row(row.cells, klasses[k])
  def test(t,row):    
    return nbClassify(t,row,klasses)
  t,logs = ilearn(f,test,train)
  for k in klasses:
    for what in ["pd","pf","prec","f","g"]:
      nums=[]
      for era,log in logs.items():
        score = log.scores()
        if k in score:
          nums += [(era,score[k][what])]
      myScatter(nums,xtxt="era",ytxt=what,f=k+what + ".pdf")
  return t

def nbClassify(t,row,klasses):
  m = the.NB.m
  k = the.NB.k
  guess, best, nh = None, -10**32, len(klasses)
  for this,klass in klasses.items():
    like = prior = (klass.n + k ) / (t.n + k * nh)
    for y,hdr in cells(row, klass.inSym):
      like *= (hdr.cnt(y) + (m*prior)) / (klass.n+m)
    for y,hdr in cells(row, klass.inNum):
      like *= hdr.pdf(y)
    if like > best:
      guess, best = this, like
  return guess


def myScatter(lst,xtxt="",ytxt="",f="out.pdf"):
  import matplotlib
  import matplotlib.pyplot as plt
  from matplotlib.backends.backend_agg \
       import FigureCanvasAgg as FigureCanvas
  from matplotlib.figure import Figure
  import numpy
  asnum   = numpy.array
  x,y    = asnum([z[0] for z in lst]), \
            asnum([z[1] for z in lst])
  fig    = Figure(figsize=(4,4))
  canvas = FigureCanvas(fig)
  ax     = fig.add_subplot(111)
  ax.set_xlabel(xtxt,fontsize=9)
  ax.set_ylabel(ytxt,fontsize=9)
  ax.grid(True,linestyle='-',color='0.75')
  #ax.set_xlim((-0.02,1.02))
  #ax.set_ylim((-0.02,1.02))
  cm = plt.cm.get_cmap('RdYlGn')
  ax.scatter(x,y,cmap=cm,edgecolors='none')
  print(f)
  canvas.print_figure(f,dpi=500)


    
