# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 23:14:24 2019

@author: Hussyvel int Test
 Reduce Function
Possible Solution below
"""

from fractions import Fraction
from functools import reduce
def product(fracs):
    t = reduce(lambda x,y: x*y,fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)