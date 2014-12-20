# libeg

This file is part of LEANER where say that data mining is easy:

1. Find some crap;
2. Cut the crap;
3. Go to step 1.

Want to know more? 

+ Download [libeg.py](https://github.com/ai-se/timm/blob/master/leaner/src/libeg.py)
+ Read our [home](README.md) page.

____


# General stuff (demos)

## Random stuff

````python
def lst(): return list('0123456789')

seed(1)
l1= shuffle(lst())
print(l1)
print(shuffle(lst()))
seed(1)
l2=shuffle(lst())
print('Resetting seed replicated old results:',
    l1==l2)
````

## Iterator stuff

````python
for one,two in pairs(lst()):
  print('one',one,'two',two)
````

## Stats stuff

````python
seed(1)
lst1=[r() for _ in xrange(1000)]
lst2=[r()**1.2 for _ in xrange(1000)]
print('big difference:',
      1==cliffsDelta(lst1,lst2))
lst3=[r() for _ in xrange(1000)]
print('small difference:',
      0==cliffsDelta(lst1,lst2))
````

## Printing stuff

````python
````
