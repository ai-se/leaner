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
    buffer = 128,
    points = 3,
    # Thresholds are from http://goo.gl/25bAh9
    dull = [0.147, 0.33, 0.474][1]
  ).update(**d)

