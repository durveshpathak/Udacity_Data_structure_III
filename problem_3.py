#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:14:55 2019

@author: durvesh
"""

def mergesort(items):
    
    if len(items) <=1:
        return items
    
    midpoint = len(items)//2
    
    left =  items[:midpoint]
    right = items[midpoint:]
    
    left_array = mergesort(left)
    right_array = mergesort(right)
    
    return merge(left_array,right_array)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index <len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index +=1
            
        else:
            merged.append(right[right_index])
            right_index +=1
            
    merged += left[left_index:]
    merged += right[right_index:]
    return merged

def rearrange_elements(arr):
    sorted_array = mergesort(arr)
    lhl = []
    rhl = []
    for i in range(0,len(sorted_array)):
        if i%2 == 0:
            lhl.append(str(sorted_array[i]))
        else:
            rhl.append(str(sorted_array[i]))
            
    return "".join(lhl), "".join(rhl)

#Test Case 1
print(rearrange_elements([4,6,2,5,9,8]))
#('964', '852')

#Test Case 2
print(rearrange_elements([9,9,9,9,9,9,9,9,9,9,9,9,9]))
#('9999999', '999999')

#Test Case 2
print(rearrange_elements([]))
#('', '')

            