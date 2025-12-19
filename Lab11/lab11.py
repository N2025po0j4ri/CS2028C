## Lab 11 Cache

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address

# Module 11 Lab Required Questions
class LRUCache:
    def __init__(self, max_size):
        self.ht = {}            # Dictionary to store key-value pairs
        self.q = Queue()        # Queue to maintain the order of recently used keys
        self.max_size = max_size    # Maximum size of the cache
        self.current_size = 0   # Current number of items in the cache
    
    def put(self, key, value):
        if key in self.ht:
            # If key already exists, update its value and move it to the front of the queue
            node = self.ht[key].node
            node.value = value
            self.q.remove(key)  # Remove the key from the queue
        elif self.current_size >= self.max_size:
            # If cache is full, remove the least recently used item
            oldest_key = self.q.dequeue()
            if oldest_key is not None:
                del self.ht[oldest_key]  # Delete the oldest key-value pair from ht
                self.current_size -= 1
        
        # Add the new entry to the cache
        new_node = Node(key)
        self.q.enqueue(key)
        self.ht[key] = CacheEntry(key, value, new_node)
        self.current_size += 1

class CacheEntry:
    def __init__(self, key, data, node):
        self.key = key
        self.value = data
        self.node = node

def CacheLookup(cache, key):
    """ Look up a key in the LRUCache and return its value if found, else None. """
    if key in cache.ht:
        return cache.ht[key].value
    else:
        return None

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None
    
    def enqueue(self, key):
        node = Node(key)
        if self.back is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            node.prev = self.back
            self.back = node
        self.size += 1
    
    def dequeue(self):
        if self.front is None:
            return None
        key = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.back = None
        else:
            self.front.prev = None
        self.size -= 1
        return key

    def remove(self, key):
        current = self.front
        while current is not None:
            if current.value == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if self.front == current:
                    self.front = current.next
                if self.back == current:
                    self.back = current.prev
                self.size -= 1
                return
            current = current.next

def number_of_hits(c, lst):
    """
    This function will take a long list of digits and use a small cache to test how likely
    digits are reused in near future. If the digits are truly random then the number of hits 
    should approach the length of list times the ratio of size of cache to the number 
    of possible digits. In our examples below this ratio is 3/10. 
    >>> c1 = LRUCache(3)
    >>> list1 = [int(c) for c in str(2**10000)]
    >>> len(list1)
    3011
    >>> number_of_hits(c1, list1)
    879
    >>> c2 = LRUCache(3)
    >>> list2 = [int(c) for c in str(3**10000)]
    >>> len(list2)
    4772
    >>> number_of_hits(c2, list2)
    1448
    """
    hits_count = 0
    for digit in lst:
        value = CacheLookup(c, digit)
        if value is not None:
            hits_count += 1
            # Update the position in the queue to reflect recent usage
            c.q.remove(digit)  # Remove the digit from the queue
            c.q.enqueue(digit)  # Enqueue it again to update its position
        else:
            c.put(digit, True)  # Add the digit to the cache as a placeholder
            
    return hits_count

# Initialize slowtable
import math  
slowtable = dict() 
for i in range(0, 11):
    slowtable[i] = math.cos(i)

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)


