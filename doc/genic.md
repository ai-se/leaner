
<small>_This file is part of LEANER. To know more, view the source code [genic.py](../src/genic.py) or read our [home](https://github.com/ai-se/leaner) page._</small>


data/diabetes2.csv (1.5M records).
caught in last gen =77%

gen | caughtLast | caughtAll | dob     | $preg | $plas  | $pres | $skin | $insu  | $mass | $pedi | $age  | =class        
1   | 205        | 390       | 1571001 | 2.04  | 97.08  | 65.03 | 23.25 | 52.6   | 29.19 | 0.35  | 24.14 | testednegative
2   | 146        | 2408      | 1560001 | 3.77  | 117.73 | 74.08 | 0.79  | 3.86   | 31.04 | 0.4   | 31.84 | testedpositive
3   | 119        | 824       | 1566001 | 7.54  | 142.17 | 78.47 | 7.53  | 16.58  | 29.72 | 0.46  | 52.1  | testednegative
4   | 109        | 252       | 1571002 | 2.39  | 145.63 | 73.09 | 30.13 | 201.47 | 34.58 | 0.35  | 28.57 | testednegative
5   | 106        | 2690      | 1554001 | 8.03  | 106.6  | 76.56 | 32.07 | 64.18  | 34.63 | 0.41  | 40.84 | testednegative
6   | 85         | 654       | 1569002 | 1.62  | 118.5  | 70.76 | 33.44 | 119.23 | 36.16 | 0.93  | 26.23 | testedpositive
genic0 {:buffer=500 :era=1000 :k=8 :klass== :num=$ :seed=1 :tiny=halfEraDivK}
rows0 {:bad=(["\' \t\r\n]|#.*) :sep=, :skip=?}

real	3m25.949s
user	3m7.403s
sys	0m2.315s
````python
````
