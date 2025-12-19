# CS2028 Lab 04 - Required Questions

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value=None):
        self.head = Node(value) if value is not None else None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("pop from an empty stack")
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if self.head is None:
            raise IndexError("peek from an empty stack")
        return self.head.value

#RQ1
def peek(s):
    """Return the value at the top of stack s without modifying the stack s.
    
    >>> s = Stack(10)
    >>> s.push(1)
    >>> s.push(2)
    >>> peek(s)
    2
    >>> s.pop()
    2
    >>> peek(s)
    1
    """
    if s.head is None:
        raise IndexError("peek from an empty stack")
    return s.head.value

#RQ2
def stack_twice(a, s):
    """Takes each value in an array a and pushes two copies onto the stack s 
    >>> a = np.array(range(5), int)
    >>> s = Stack(2*len(a))
    >>> stack_twice(a, s)
    >>> for i in range(10): print(s.pop(), end=' ')
    4 4 3 3 2 2 1 1 0 0 
    """
    for value in a:
        s.push(value)
        s.push(value)
        
def dequeue(queue):
    """Removes and returns the first element of the queue."""
    return queue.pop(0)

#RQ3
def queue_numbers(n):
    """ Creates a queue with the values from 1 to n in that order.
    >>> q= queue_numbers(5)
    >>> dequeue(q) == 1
    True
    >>> dequeue(q) ==  2
    True
    >>> dequeue(q) ==  3
    True
    """
    return list(range(1, n+1))

#RQ4
def balanced(string):
    """Test whether or not the string is a string with balanced parentheses.
    Your function should use a stack data structure.
    >>> balanced('()()')
    True
    >>> balanced('(()))')
    False
    >>> balanced('(()())')
    True
    """
    stack = []  # Initialize an empty stack
    
    for char in string:
        if char == '(':
            stack.append(char)  # Push opening parenthesis onto the stack
        elif char == ')':
            if not stack or stack[-1] != '(':  # If stack is empty or top doesn't match
                return False
            stack.pop()  # Pop matching opening parenthesis from the stack
    
    return len(stack) == 0  # If stack is empty, all parentheses are balanced 

import numpy as np
if __name__ == "__main__":
   import doctest
   doctest.testmod(verbose=True)
