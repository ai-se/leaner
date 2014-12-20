# config

This file is part of LEANER where say that data mining is easy:

1. Find some crap;
2. Cut the crap;
3. Go to step 1.

Want to know more? 

+ Download [config.py](https://github.com/ai-se/timm/blob/master/leaner/src/config.py)
+ Read our [home](README.md) page.

____


# Configuration Control

Stores the settings that can change how well we can learn things.

## Config Support Code

Must come first.

````python
from boot import *

@setting
def LIB(**d): return o(
    buffer = 128,
    points = 3,
    # Thresholds are from http://goo.gl/25bAh9
    dull = [0.147, 0.33, 0.474][1]
  ).update(**d)

````
