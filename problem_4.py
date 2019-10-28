#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:31:39 2019

@author: durvesh
"""

def single_traverse_sort(input):
    count_zero = 0
    count_one = 0
    count_two = 0
    output = []
    for num in input:
        if num == 0:
            count_zero +=1
        if num ==1:
            count_one +=1
        if num ==2:
            count_two +=1
    for i in range(0,count_zero):
        output.append(0)
    for i in range(0,count_one):
        output.append(1)
    for i in range(0,count_two):
        output.append(2)
        
    return output

#Test Case 1
print(single_traverse_sort([0,0,0,0,2,0,1,2,2,1,1,0]))
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2]

#Test Case 2
print(single_traverse_sort([0,1,2,0,2,0,1,2,2,1,1,1]))
[0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2]

#Test Case 2
print(single_traverse_sort([]))
#[]