from __future__ import division,print_function
import sys
sys.dont_write_bytecode=True

from lib import *

@go
def _go():
  "Should a,b and no c values."
  x=o(a=1,b=2,_c=2)
  print(x)

@go
def _shuffle():
  rseed(1)
  print(shuffle(list('abcdefg')))

@go
def _say():
 say(1,2,'b',say)

 @go
 def _g():
   lst = [r() for _ in xrange(10)]
   print(lst)
   print(g(lst))

@go
def _printm():
  header=[["name","age","shoesize"],
          ["----","---","--------"]]
  data = [["Usually what is the dumpster?",
           "Denver dumpster is a metal container",
           "that is utilized for waste"],
          ["and developed in media blast Hallsboro",
           "NC such a way that it enables the",
           "emptying of the waste into rubbish",
           "Media Blasting Guys trucks. Hamlet NC",
           "media blaster A Denver roll of"],
          ["container on the other hand is",
           "basically a dumpster media blast",
           "Hobucken NC with an open top" ]]
  printm(header+data)
  
