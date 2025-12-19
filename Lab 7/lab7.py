# CS2023 - Lab07 - Heaps - Required Questions

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address


## Starter Code for Lab 07
class Heap:
    def __init__(self, maxsize):    
        self.maxsize = maxsize
        self.array = np.zeros(maxsize + 1, dtype=int)
        self.last_index = 0
        self.size = 0
    

def heap_remove_max(heap):
    if heap.last_index == 0:  return None
    # Swap out the root for the last element and shrink heap.  
    result = heap.array[1]
    heap.array[1] = heap.array[heap.last_index]
    heap.array[heap.last_index] = -1
    heap.last_index = heap.last_index - 1

    # Bubble the new root down.
    i = 1
    while i <= heap.last_index:
        swap = i
        if (2*i <= heap.last_index) and (heap.array[swap] < heap.array[2*i]):
            swap = 2*i
        if (2*i+1 <= heap.last_index) and (heap.array[swap] < heap.array[2*i+1]):
            swap = 2*i+1
        if i != swap:
            temp = heap.array[i]
            heap.array[i] = heap.array[swap]
            heap.array[swap] = temp
            i = swap
        else:   break
    return result

def heap_insert(heap, value):  
    if heap.last_index == heap.maxsize:
        return "Increase Heap size"
    heap.last_index += 1
    heap.array[heap.last_index] = value
    current = heap.last_index
    parent = current//2
    while (parent >= 1) and (heap.array[parent] < heap.array[current]):
        temp = heap.array[parent]
        heap.array[parent] = heap.array[current]
        heap.array[current] = temp		
        current = parent
        parent = current // 2

def heapsort_dec(a):
    """ Sorts an array a in decreasing order using MaxHeap
    >>> result = heapsort_dec([1,2,3,4,5])
    >>> result
    array([5, 4, 3, 2, 1])
    """
    n = len(a)
    tmp_heap = Heap(n)
    result = np.zeros(n, dtype = int)
    j = 0
    while j < n:
        heap_insert(tmp_heap, a[j])
        j = j + 1
    j = 0
    while j < n:
        result[j] = heap_remove_max(tmp_heap)
        j = j + 1
    return result

## End of Starter Code 

def resize_heap(minheap):
    """ Helper function to double the size of the heap array """
    new_array = np.zeros(2 * minheap.maxsize + 1, dtype=int)
    new_array[:minheap.maxsize + 1] = minheap.array
    minheap.array = new_array
    minheap.maxsize = 2 * minheap.maxsize
    
#RQ1 Implement the following key function for a working MinHeap
def min_heap_insert(minheap, value):
    """ Define a function min_heap_insert part of a MinHeap implementation
    >>> h = Heap(3)
    >>> min_heap_insert(h, 11)
    >>> min_heap_insert(h, 10)
    >>> min_heap_insert(h, 9)
    >>> h.array
    array([ 0,  9, 11, 10])
    """
    if minheap.last_index == minheap.maxsize:
        resize_heap(minheap)
    
    minheap.last_index += 1
    current = minheap.last_index
    minheap.array[minheap.last_index] = value
    
    while current > 1:
        parent = current // 2
        
        if minheap.array[parent] >= minheap.array[current]:
            minheap.array[parent], minheap.array[current] = minheap.array[current], minheap.array[parent]
            current = parent
        else:
            break
    
        
#RQ2 Implement the following key function for working MinHeap

def heap_remove_min(minheap): 
    """ Define a function heap_remove_min part of a MinHeap implementation
    >>> h = Heap(3)
    >>> min_heap_insert(h, 11)
    >>> min_heap_insert(h, 10)
    >>> min_heap_insert(h, 9)
    >>> result = heap_remove_min(h)
    >>> result
    9
    >>> h.array
    array([ 0, 10, 11, -1])
    """
    if minheap.last_index == 0:
        return None
    result = minheap.array[1]
    minheap.array[1] = minheap.array[minheap.last_index]
    minheap.array[minheap.last_index] = -1
    minheap.last_index -= 1
    
    i = 1
    while i <= minheap.last_index:
        swap = i
        left_child = 2*i
        right_child = 2*i + 1
        if left_child <= minheap.last_index and minheap.array[left_child] < minheap.array[swap]:
            swap = left_child
        if right_child <= minheap.last_index and minheap.array[right_child] < minheap.array[swap]:
            swap = right_child
        if i != swap:
            minheap.array[i], minheap.array[swap] = minheap.array[swap], minheap.array[i]
            i = swap
        else:
            break
    return result
       
#RQ3 Implement the following sorting method using a MinHeap

def heapsort_inc(a):
    """ Sorts an array a in increasing order using MinHeap implementation
    >>> result = heapsort_inc([5,1,2,4,3])
    >>> result
    array([1, 2, 3, 4, 5])
    """
    n = len(a)
    tmp_heap = Heap(n)
    result = np.zeros(n, dtype=int)
    
    # Insert all elements into the MinHeap
    for num in a:
        min_heap_insert(tmp_heap, num)
    
    # Extract elements from MinHeap to get sorted order
    for j in range(n):
        result[j] = heap_remove_min(tmp_heap)
    return result
   
   
import numpy as np
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
