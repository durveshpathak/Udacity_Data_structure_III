#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:20:44 2019

@author: durvesh
"""

def binary_search_rotated(arr, target):
    n = len(arr)
    pivot = rotation_point(arr, 0, n-1)
    
    if pivot == -1:
        return binarysearch(arr,target,0,n-1)
    
    if arr[pivot] == target:
        return pivot
    if arr[0] <= target:
        return binarysearch(arr,target,0,pivot-1)
    
    return binarysearch(arr, target, pivot+1, n-1)

def binarysearch(arr, key, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index)//2

    if arr[mid_index] == key:
        return mid_index

    elif key > arr[mid_index]:
        return binarysearch(arr, key, mid_index + 1, end_index)
    else:
        return binarysearch(arr,key, start_index,mid_index-1)

def rotation_point(arr, low, high):
    
    mid = (low+high)//2
    
    if high < low:
        return -1
    if high == low:
        return low
    
    if arr[mid] > arr[mid+1]:
        return mid
    if arr[mid] < arr[mid-1]:
        return mid-1
    if arr[low] > arr[mid]:
        return rotation_point(arr, low, mid-1)
    else:
        return rotation_point(arr,mid+1, high)

# Test case 1
print(binary_search_rotated([4,5,6,7,8,9,1,2,3,4],3))
#8

# Test case 2
print(binary_search_rotated([4,5,6,7,8,9,1,2,3,4],15))
#-1

# Test case 3
print(binary_search_rotated([],3))
#-1