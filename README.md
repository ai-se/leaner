
# Data Mining: a  LEANER approach

<img align=right width=300 src="etc/img/leanRoboToolboxSmall.jpg">
LEANER is a data mining toolbox. It is the _least_  Python I can write to 
_most_ illustrate  data mining. Turns out,
data mining is easy if
you follow three simple rules:

1. Find some crap;
2. Cut the crap;
3. Go to step 1.

## Contents

+ [boot](doc/boot.md):  Boot code: stuff needed before anything else
+ [bore](doc/bore.md):  BORE (best or rest)
+ [cocomo](doc/cocomo.md):  Software Effort and Risk Estimation
+ [cocomo](doc/cocomo.md):  vlow low nom high vhigh xhigh
+ [cocomoeg](doc/cocomoeg.md):  Test Cases for COCOMO
+ [column](doc/column.md):  Defining columns
+ [column](doc/column.md):  Thresholds are from http://goo.gl/25bAh9
+ [columneg](doc/columneg.md):  Column stuff (demos)
+ [columns](doc/columns.md):  Handling Columns of Data
+ [config](doc/config.md):  Configuration Control
+ [de](doc/de.md):  Simple Differential Evolution
+ [lib](doc/lib.md):  General stuff
+ [libeg](doc/libeg.md):  General stuff (demos)
+ [ranker](doc/ranker.md):  add in scorerd. abcd mre, lift

## Installation

LEANER uses a standard UNIX environment (with git,
make, python 2.7+, bash, awk, etc).  To install and test, do
the following:


```
git clone https://github.com/ai-se/leaner.git
make test 
```

## Current Status

Work in progress. Started Dec 17 2014. But I got a cool logo!

## How to Read This Code

__this section needs work__

+ settings. specified locally per file, held in a global for (a) printing (b) tuning purposes.  not passed down (tedious for long chains of sub-calls)
+ extensive use of iterators, list comprehensions, decorators. read up on it!
+ write less classes: o is good
+ N-1 globals better than N. we have only one "the"
+ many file.py has fileeg.py. each eg starts with @go, fired on loading
+ 2 spaces, "self" ==> "i"

## Why Read This Code

__this section needs work__

+ Decades of research, data mining is simple.  Much to much made of the complexity of data mining when
the truth is, it is much simpler than that (particulalry in the arena of statistical comparisons).
+ Many books offer small examples of different kinds of data miners. 
  Wanted something different- something that draws all the methods together. Seeing  a new synthesis. Not some increasing focus on one discipline but building tools that
  work on many fields. Look closer at the pieces top build a new toolkit whose whole is more
  than the parts.
+ My students can, after 6 to 12 weeks, build and modify start of the art devices. 
A research career marked by many masters with journal publications (novel results, short time). 
Do you want to be that productive?  You can!
+ Thou shalt not click.
+ Not enough to use these tools, need to look inside them (at least once). The shepperd results.
+ Mix and match. e.g. data mining and moea closer than you might expect from reading the literature. 
+ Fun!

## License

Copyright (c) 2015 Tim Menzies  
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

