
# Lib.py

This file defines basic conventions and low-level
code to support "open software science" (OpeSS).

An open software scientist analyzes and shares
software artifacts with the goal of generating
libraries of trusted software tools.  Their
conclusions are repeatable, improvable and
refutable.

Tools, not just opions..

Open software scientists use literature
programming. Their code comments describe
experiments (simulation, data mining, etc) that
execute within their code.  That code does not just
run, it reports opinions.  It comments on whether X
is better than Y.

To encourage sharing and an open analysis of all concluions,
OpeSS uses open source tools. All work is stored on-line
in repositories that support commenting, forking, and merging.

The world we live in today is much more a man-made,
or artificial, world than it is a natural
world. Almost every element in our environment shows
evidence of human artifice.

Because of its abstract character and its symbol
manipulating generality, the digital computer has
greatly extended the range of systems whose behavior
can be imitated. Generally we now call the imitation
"simulation," and we try to understand the imitated
system by testing the simulation in a variety of
simulated, or imitated, environments.  Artificial
systems and adaptive systems have properties that
make them particularly susceptible to simulation via
simplified models.

A frequently asked question is how can a simulation
ever tell us anything that we do not already know?
The obvious point is that, even when we have correct
premises, it may be very difficult to discover what
they imply. All correct reasoning is a grand system
of tautologies, but only God can make direct use of
that fact. The rest of us must painstakingly and
fallibly tease out the consequences of our
assumptions.

In science and engineering the study of
"systems" is an increasingly popular
activity. Its popularity is more a
response to a pressing need for
synthesizing and analyzing complexity
than it is to any large development of a
body of knowledge and technique for
dealing with complexity. If this
popularity is to be more than a fad,
necessity will have to mother invention
and provide substance to go with the
name.


## Principles

### Shareable

+ Code starts with some open source license statement.
+ Code stored in some downloadable public space (e.g. Github).
+ Coded in some widely used language (e.g. Python) with extensive 
  on-line tutorialsl e.g. [Stackoverflow.com](http://stackoverflow.com/questions/tagged/python).

### Readable

#### Succinct

Not arcane, but lots of little short and useful code snippets. 

#### Abstract

Heavy use of abstraction to simplify processing of low-level details.

#### Succinct

Deliver features, not code. N-1 lines of code better than N. Write your code then cut it in half. YAGNI! YAGNI!

#### Functional more Object-Oriented

_(BEGIN PERSONNEL BIAS)_

N-1 classes better than N. Give us this day our daily lambda. 

Why? Well functional programemers can define and code a dozen useful patterns in the time it
takes a pure-OO guy to code one class.

#### Commented

Comments tell a story. Describe each function in terms
of some idiom (small thing) or pattern (larger thing)
describing something that someone else other than
the programmer might actually care about

Code written to be included into a two column paper:

+ All comments written in multiline strings and in 
  Pandoc style markdown.
      + File contains only one H1 header.
+ No line longer than 52 characters.  Which means
  for a language like Python:
    + _Self_ replaced with "_i_".
    + Indented with two characters.

### Sensible

Using Python 2.7 (cause of compatability issues).
Adopt the future `print` and `division`
functions. Do not write spurious _.pyc_ files.
For examples of the use of these idioms, see top of this file.
