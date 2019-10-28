#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:41:08 2019

@author: durvesh
"""
    
            
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    min = 0
    max = 0
    
    for num in ints:
        if num<min:
            min = num
        if num>max:
            max = num
    return min, max

## Example Test Case of Ten Integers
import random
#test Case 1
l = [i for i in range(0, 8)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 7) == get_min_max(l)) else "Fail")
# Pass

#Test Case 2
l = [i for i in range(0, 50)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 49) == get_min_max(l)) else "Fail")
# Pass

#Test Case 3
l = [i for i in range(-47, 100)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((-47, 99) == get_min_max(l)) else "Fail")
# Pass

#Test Case 0
l = [i for i in range(0,0)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((None) == get_min_max(l)) else "Fail")
# Pass
