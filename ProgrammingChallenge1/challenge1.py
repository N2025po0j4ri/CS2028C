#!/usr/bin/env python3
# CS2028 Lab 03 - Required Questions

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node
        
def insert_after(node, new_node):
    new_node.next = node.next
    new_node.previous = node
    if node.next:
        node.next.previous = new_node
    node.next = new_node
      
def find_x_node(head1, head2):
    """
    A=3->7->8->10
    B=1->8->10
    >>> headA = Node(3); node7 = Node(7); node8 = Node(8); node10 = Node(10)
    >>> headA.next = node7; node7.next = node8
    >>> node8.next = node10; headB = Node(1); headB.next = node8
    >>> xnode = find_x_node(headA, headB)
    >>> xnode.value
    8
    >>> head1 = Node(0); prev1 = head1
    >>> for i in range(1, 10):
    ...    new1 = Node(i)
    ...    if i == 5: mid1 = new1
    ...    insert_after(prev1, new1)
    ...    prev1 = new1
    >>> head2 = Node(10); prev2 = head2
    >>> for i in range(11, 30):
    ...    new2 = Node(i)
    ...    insert_after(prev2, new2)
    ...    prev2 = new2
    >>> prev2.next = mid1
    >>> xnode = find_x_node(head1, head2)
    >>> xnode.value
    5
    """
    '''
    find_node = set()
    curr = head1
    while curr:
        find_node.add(curr)
        curr = curr.next
    curr = head2
    while curr:
        if curr in find_node:
            return curr
        curr = curr.next
    return None
    '''
    ptr1 = head1
    ptr2 = head2

    while ptr1 != ptr2:
        ptr1 = ptr1.next if ptr1 else head2
        ptr2 = ptr2.next if ptr2 else head1

    return ptr1

import math
import numpy as np
import doctest
if __name__ == "__main__":
   doctest.testmod(verbose=True)
