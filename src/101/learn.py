from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from table import *
from abcd  import *

def ilearn(src, test, train, report=True):
  logs = {}
  last = Abcd()
  for t,rows,era in eras(src):
    if era:
      now = logs[era] = last.copy()
    else:
      now = Abcd()
    for row in rows:
      k = theKlass(t,row)
      if era:
        predicted = test(t,row)
        now(k, predicted)
      train(t,row,k)
    last = now
  return t,logs

def ilearnReport(f,klasses,logs):
  for k in klasses:
    for what in ["pd","pf","prec","f","g"]:
       nums=[]
       for era,log in logs.items():
         score = log.scores()
         if k in score:
           nums += [(era*the.TABLE.era,score[k][what])]
       myScatter(nums,xtxt="training examples",
                 ytxt=what,f=k+what + ".pdf")
       
def myScatter(lst,xtxt="",ytxt="",f="out.pdf"):
  import matplotlib
  import matplotlib.pyplot as plt
  from matplotlib.backends.backend_agg \
       import FigureCanvasAgg as FigureCanvas
  from matplotlib.figure import Figure
  import numpy
  from matplotlib import rcParams
  rcParams.update({'figure.autolayout': True})
  asnum  = numpy.array
  x,y    = asnum([z[0] for z in lst]), \
            asnum([z[1] for z in lst])
  fig    = Figure(figsize=(4,2))
  canvas = FigureCanvas(fig)
  ax     = fig.add_subplot(111)
  ax.set_xlabel(xtxt,fontsize=9)
  ax.set_ylabel(ytxt,fontsize=9)
  ax.grid(True,linestyle='-',color='0.75')
  ax.set_ylim((-2,102))
  cm = plt.cm.get_cmap('RdYlGn')
  plt.ylim(-5,100)
  ax.plot(x,y,marker='o', linestyle='--', color='r', label='Square')
  ax.tick_params(axis='both', which='major', labelsize=9)
  ax.tick_params(axis='both', which='minor', labelsize=9)
  print(f)
  canvas.print_figure(f,dpi=500)
