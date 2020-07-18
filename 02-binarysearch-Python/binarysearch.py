"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(arr, value):
    mins = 0
    maxs = len(arr) - 1
    while mins <= maxs: 
  
        mid = mins + (maxs) - 1// 2; 
        if arr[mid] == value: 
            return mid 
  
        elif arr[mid] < value: 
            mins = mid + 1
        else: 
            maxs = mid - 1

    return -1
