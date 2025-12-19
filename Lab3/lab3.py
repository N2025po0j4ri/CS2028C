#!/usr/bin/env python3
# CS2028 Lab 03 - Required Questions

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address


#RQ1
def array_triple(old_array):
    """ This function copies an array and 
    returns a new array of thrice the original size.
    >>> x = np.array(range(10))
    >>> len(x)
    10
    >>> newx = array_triple(x)
    >>> len(newx)
    30
    """
    length = len(old_array)
    new_array = np.zeros(length*3)
    for j in range(length):
        new_array[j] = old_array[j]
    return new_array

class Linked_Node:
   def __init__(self, value=None):
      self.value = value
      self.next = None
      self.previous =None

#RQ2
def insert_before(first_node,second_node):
    """ This function inserts the second_node before the first_node
    which is a node in a doubly linked list.
    >>> A = Linked_Node("A"); B =Linked_Node("B"); C=Linked_Node("C")
    >>> insert_before(A,B); insert_before (A,C)
    >>> B.next.value =='C'
    True
    >>> C.next.value == 'A'
    True
    >>> A.previous.value =='C'
    True
    >>> C.previous.value =='B'
    True
    """    
    if first_node is None or second_node is None:
        raise ValueError("Nodes cannot be None")
    
    # Check if second_node is already before first_node
    if first_node.previous == second_node:
        return
    
    # Update links for second_node
    second_node.previous = first_node.previous
    second_node.next = first_node
    
    # Update links for first_node
    if first_node.previous is not None:
        first_node.previous.next = second_node
    first_node.previous = second_node

#RQ3
def linked_list_insert_duplicates(head,  indexlist, value):
    """ This function inserts the several duplicates of value 
      with index values coming from indexlist. So the total number of copies
      inserted is the same as the length of the indexlist. The duplicate nodes should
      be inserted as if they all happened at the same time.
      
    >>> A = Linked_Node("A"); B =Linked_Node("B");C=Linked_Node("C")
    >>> insert_before(A,B); insert_before (A,C)
    >>> head = linked_list_insert_duplicates(B,  [0,2], 'D')
    >>> head.value == 'D'
    True
    >>> head.next.value == 'B'
    True
    >>> head.next.next.value == 'C'
    True
    >>> head.next.next.next.value == 'D'
    True
    >>> head.next.next.next.next.value == 'A'
    True
    """
    if not head or not indexlist:
        return head

    current = head
    prev = None
    index = 0

    while current:
        if index in indexlist:
            new_node = Linked_Node(value)
            new_node.next = current
            if prev:
                prev.next = new_node
            else:
                head = new_node
            prev = new_node
        else:
            prev = current
        current = current.next
        index += 1

    return head
    
#RQ4
def linked_list_count_duplicates(head_node, value):
    """ This function counts and returns the number of duplicates of value 
      in the linked list with head head_node.
    >>> A = Linked_Node("A"); B =Linked_Node("B");C=Linked_Node("C")
    >>> insert_before(A,B); insert_before (A,C)
    >>> head = linked_list_insert_duplicates(B,  [0,2], 'D')
    >>> linked_list_count_duplicates(head, 'D')
    2
    >>> linked_list_count_duplicates(head, 'E')
    0
    """
    count_dup = 0
    current = head_node
    
    while current:
        if current.value == value:
            count_dup+=1
        current = current.next

    return count_dup

import math
import numpy as np
import doctest
if __name__ == "__main__":
   doctest.testmod(verbose=True)
