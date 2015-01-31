from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

r=random.random

seed=random.seed

seed(1)
any=random.choice
def anys(lst,n):
    return [any(lst) for _ in xrange(n)]
    
class Row:
    def __init__(i,lst):
        i.cells=lst
    def __hash__(i): return id(i)
    
all =  [tuple([int(r()*5) for _ in xrange(10)] )
       for _ in xrange(10000)]
       
some1 = anys(all, 50)
some2 = anys(all, 50)

 
def fand(l1,l2):
    return set(l1) & set(l2)
    
def frands(l):
    return reduce(lst,fans)
   

    

some3=fand(some1,some2)
print(len(some3))