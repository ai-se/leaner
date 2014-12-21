from __future__ import division,print_function
import sys
sys.dont_write_bytecode =True

"""

# Configuration Control

Stores the settings that can change how well we can learn things.

## Config Support Code

Must come first.

"""
from boot import *

@setting
def LIB(**d): return o(
    # Thresholds are from http://goo.gl/25bAh9
    dull = [0.147, 0.33, 0.474][0]
  ).update(**d)

@setting
def COL(**d): return o(
    # Thresholds are from http://goo.gl/25bAh9
    buffer = 128,
    m = 2,
    k = 1
  ).update(**d)

