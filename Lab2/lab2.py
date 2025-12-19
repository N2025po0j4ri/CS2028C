#!/usr/bin/env python3
# CS2028 Lab 02 - Required Questions

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address

#  RQ1
def binary_search (a, target):
    """ Use binary search on an array a to locate the target and returning 
    the index  of the target. If the target is not an array element, then return -1.
    >>> a = np.array(range(100))
    >>> binary_search(a,7)
    7
    >>> a = np.array(range(50, 100))
    >>> binary_search(a,71)
    21
    >>> binary_search(a,101)
    -1
    """
    #Initialized the boundaries of the search range
    left = 0
    right = len(a) - 1
    
    #Keep searching while the search range is valid
    while left <= right:
        #Calculate the midpoint of the search range
        mid = (left + right) // 2
        
        #Check if the target is at the midpoint
        if a[mid] == target:
            return mid
        
        #If the target is smaller, search the left half
        elif a[mid] > target:
            right = mid - 1
            
        #If the target is larger, serach the right half
        else: 
            left = mid + 1
    return -1

#RQ2
def binary_insert(a, target):
    """ Use binary search on the array a to locate the target and return
    the index of the target. If the target is not present in the array, replace the 
    closest value less than the target with the target in the array, and return the index.
    If the target is smaller than all array elements return -1.
    >>> a = np.array(range(10),float)
    >>> binary_insert(a,7.0)
    7
    >>> binary_insert(a,7.5)
    7
    >>> a[7]
    7.5
    >>> binary_insert(a,-5)
    -1
    """
    # Edge case: if the target is smaller than all elements, return -1
    if target < a[0]:
        return -1
    
    #Initialized the boundaries of the search range
    left = 0
    right = len(a) - 1
    
    #Keep searching while the search range is valid
    while left <= right:
        
        #calculate the midpoint of the search range
        mid = (left + right) // 2
        
        #Check if the target is at the midpoint
        if a[mid] == target:
            return mid
        
        #If the target is smaller, search the left half
        elif a[mid] > target:
            right = mid - 1
            
        #If the target is larger, search the right half
        else:
            left = mid + 1
            
    #Assigns the element of a to target and returns right as the index
    a[right] = target
    return right
    
#RQ3
def bisection_root(x):
    """ Use the bisection method to compute the square root of x correct to 4 decimal places (i.e., 
    difference is at most 1e-4.
    >>> r = bisection_root(100)
    >>> abs(r - 10) < 1e-4
    True
    >>> r = bisection_root(2)
    >>> abs(r - 1.41421) < 1e-4
    True
    >>> r = bisection_root(3)
    >>> abs(r - 1.73205) < 1e-4
    True
    """
    epsilon = 1e-4
    low = 0
    # Ensure high is at least 1 or x
    high = max(1, x)
    guess = (low + high) / 2

    while abs(guess ** 2 - x) > epsilon:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    # Changed round to 4 to ensure correct rounding
    return round(guess, 4)

#RQ4
def bisection_root_small(x):
    """ Use the bisection method to compute the square root of a number 0 < x < 1 
    correct to 4 decimal places, i.e., difference is at most 1e-4.

    >>> r = bisection_root_small(1/100)
    >>> abs(r - 1/10) < 1e-4
    True
    >>> r = bisection_root_small(1/25)
    >>> abs(r - 1/5) < 1e-4
    True
    >>> r = bisection_root_small(1/10000)
    >>> abs(r - 1/100) < 1e-4
    True
    """
    # variables used to use bisection method
    low = 0.0
    high = 1.0
    epsilon = 1e-4

    while high - low > epsilon:
        # midpoint method to bisect
        mid = (low + high) / 2
        if mid * mid < x:
            low = mid
        else:
            high = mid

    return (low + high) / 2

#RQ5 
def Madhava_Leibniz(arg):
    """
    The Madhava–Leibniz series for pi/4 is an infinite sum of numbers 
    that is alternating series of the unit fractions of odd numbers.
    1 - 1/3 + 1/5 - 1/7 + ....
    Determine the number of terms of series needed to achieve an approximation within 
    arg of math.pi/4
    >>> Madhava_Leibniz(1e-1)
    3
    >>> Madhava_Leibniz(1e-2)
    25
    >>> Madhava_Leibniz(1e-3)
    250
    >>> Madhava_Leibniz(1e-4)
    2500
    """
    approximation = 0.0
    n_terms = 0
    sign = 1

    while abs(approximation - math.pi/4) >= arg:
        n_terms += 1
        approximation += sign * (1 / (2 * n_terms - 1))
        sign *= -1

    return n_terms

    
import math
import numpy as np
import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)
