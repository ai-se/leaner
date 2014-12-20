
<small>_This file is part of LEANER. To know more, download [config.py](https://github.com/ai-se/leaner/blob/master/src/config.py)'s source or read our [home](README.md) page._</small>



# Configuration Control

Stores the settings that can change how well we can learn things.

## Config Support Code

Must come first.

````python
from boot import *

@setting
def LIB(**d): return o(
    buffer = 128,
    # Thresholds are from http://goo.gl/25bAh9
    dull = [0.147, 0.33, 0.474][0]
  ).update(**d)

````
