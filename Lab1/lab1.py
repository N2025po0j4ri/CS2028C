""" Required questions for CS2028 Lab 1."""
## Modify this file by adding your salutation.
## Your code should be placed after each doctest (paired """  """). 
## Once you pass all the doctests, then you submit your program for credit. 

_author_ = "Nirupama Poojari"
_credits_ = ["Fred Annexstein"]
_email_ = "poojarna@mail.uc.edu" # Your email address


#RQ1
def switch_first_last(x):
    """Returns an array in which the first and last items are switched
    >>> x=np.array(range(10))
    >>> (first,last) = (x[0], x[9]) 
    >>> x = switch_first_last(x)
    >>> (first,last) == (x[9], x[0])
    True
    >>> print(x)
    [9 1 2 3 4 5 6 7 8 0]
    """
    if len(x) <= 1:
        return x
    
    # Swap the first and last elements
    x[0], x[-1] = x[-1], x[0]
    
    return x
  

#RQ2
def item_count(target, x):
    """Counts the number of times target appears in array x
    >>> x=np.zeros(10)
    >>> item_count(0, x)
    10
    >>> x=np.array(range(10))
    >>> item_count(9, x)
    1
    >>> item_count(10, x)
    0
    """
    count = np.count_nonzero(x == target)
    return count

 
#RQ3
def powers_of_2(n):
   """Returns an array of length n containing the powers of 2 from 2 to 2^n
   >>> powers_of_2(1)
   array([2], dtype=int32)
   >>> powers_of_2(2)
   array([2, 4], dtype=int32)
   >>> powers_of_2(5)
   array([ 2,  4,  8, 16, 32], dtype=int32)
   """
   x = np.arange(1, n+1)
   #return np.array(np.power(2,x).tolist())
   return np.power(2, x)
 

#RQ4
def insertion_sort_dec(a):
    """Returns an array in non-increasing order using insertion sort
    >>> x = insertion_sort_dec (np.array(range(10)))
    >>> x 
    array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    >>> x = np.array([-9, 4, -3, 8, -7, 0, -5, 6, -2, 1])
    >>> x = insertion_sort_dec (x)
    >>> x
    array([ 8,  6,  4,  1,  0, -2, -3, -5, -7, -9])
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

#RQ5
def count_diffs(x,y):
    """Returns a count of the number of differences in two arrays.
    If one array is smaller than the other then the size of the difference is 
    added to the count
    >>> c = count_diffs(np.array(range(10)),np.array(range(10)))
    >>> c
    0
    >>> c = count_diffs(np.array(range(10)),np.array(range(5)))
    >>> c
    5
    >>> c = count_diffs(np.array(range(10)),np.array([0,2,2,3]))
    >>> c
    7
    """
    min_len = min(len(x), len(y))
    diffs = np.count_nonzero(x[:min_len] != y[:min_len])
    return diffs + abs(len(x) - len(y))


import numpy as np
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
