
<small>_This file is part of LEANER. To know more, view the source code [config.py](../src/config.py) or read our [home](https://github.com/ai-se/leaner) page._</small>



# Configuration Control

Stores the settings that can change how well we can learn things.

## Config Support Code

Must come first.

````python
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

````
