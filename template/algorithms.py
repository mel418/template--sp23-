"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    # todo
    for i in range(len(a)):
        if a[i] == x:
            return i
    return None


def binary_search(a: List, x):
    # todo
    l = 0
    r = len(a)-1
    while l <= r:
        #print(a[l:r+1])
        m = (l+r) // 2
        #print(m)
        if x == a[m]: return m
        if x < a[m]:
            r = m - 1
        else:
            l = m + 1
        
    return None


def _merge(a0: List, a1: List, a: List):
    # todo
    i0 = 0  # current index of array a0
    i1 = 0  # current index of array a1
    
    for i in range(len(a)):
        if i0 >= len(a0):
            a[i] = a1[i1]
            i1 += 1
        elif i1 >= len(a1):
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1    

    


def merge_sort(a: List):
    # todo
    if len(a) <= 1:
        return a
    
    # Split the array into two halves
    mid = len(a) // 2
    a0 = a[0:mid]
    a1 = a[mid:len(a)]
    # print(a0)
    # print(a1)
    # Recursively sort each half
    (merge_sort(a0))
    (merge_sort(a1))
    
    # Merge the two sorted halves
    _merge(a0, a1, a)
    #print(a0, a1, a)
    
    


def _quick_sort_f(a: List, start, end):
    # todo
    if start >= end:
        return
    
    # Choose the first element as pivot
    pivot = a[start]
    
    # Partition the array around the pivot
    i = start + 1
    j = end
    while i <= j:
        if a[i] <= pivot:
            i += 1
        elif a[j] > pivot:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    # Move the pivot to its sorted position
    pivot_pos = j
    a[start], a[pivot_pos] = a[pivot_pos], a[start]
    
    # Recursively sort the left and right partitions
    _quick_sort_f(a, start, pivot_pos - 1)
    _quick_sort_f(a, pivot_pos + 1, end)



def _quick_sort_r(a: List, start, end):
    # todo
    if start >= end:
        return
    
    # Choose a random element as pivot
    pivot_idx = random.randint(start, end)
    pivot = a[pivot_idx]
    
    # Move the pivot to the beginning of the array
    a[start], a[pivot_idx] = a[pivot_idx], a[start]
    
    # Partition the array around the pivot
    i = start + 1
    j = end
    while i <= j:
        if a[i] <= pivot:
            i += 1
        elif a[j] > pivot:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        
    
    # Move the pivot to its sorted position
    pivot_pos = j
    a[start], a[pivot_pos] = a[pivot_pos], a[start]
    
    # Recursively sort the left and right partitions
    _quick_sort_r(a, start, pivot_pos - 1)
    _quick_sort_r(a, pivot_pos + 1, end)


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)

'''
a = [56,10,34,87,41,34,9,3]
b = [5,6,7,7,30,45,150,653]
test = [5, 4, 3, 2, 1, 0]
#binary_search(test,7)

import ArrayList
arrayA = ArrayList.ArrayList()
for el in test:
    arrayA.append(el)
#(merge_sort(b))
quick_sort(arrayA)
#print(arrayA)
'''