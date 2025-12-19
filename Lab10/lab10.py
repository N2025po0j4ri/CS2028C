## Lab 10 Hash Tables

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address

# Required Questions for Mod 10
# In this Lab you are to implement a hash table using chaining. Each 
# non-empty bin is a linked list of ListNodes containing key,value pairs.

class HashTable():
    def __init__(self,size):
        self.size= size
        self.bins = [None for _ in range(size)]

class ListNode():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

def HashFunction(key, size):
    return key % size  

#RQ1
def StringHashFunction(key_string, size):
   """
   >>> StringHashFunction("Cincinnati Bearcats",23)
   6
   >>> StringHashFunction("Morning Joe",23)
   20
   """
   CONST = 2**8 +1 # A prime number
   hash_value = 0
   for char in key_string:
       hash_value = (hash_value * CONST + ord(char)) % size
    
   return hash_value
   
       
        
def HashTableInsert(htable, key, value):
    """
    HashTableInsert inserts the key,value pair using chaining.
    1) first computes the hash_value of the key.
    2) check if the associated bin is empty and if so create a new 
    linked list with a new ListNode.
    3) if bin is not empty use a loop to check if key exists in table
    4) if the key does exist update the value., else add new ListNode 
    to the end of the linked list.
    
    >>> ht = HashTable(10)
    >>> HashTableInsert(ht, 101, "one oh one")
    >>> HashTableInsert(ht, 102, "one oh two")
    >>> HashTableInsert(ht, 102, "updated one oh two")
    >>> ht.bins[1].key 
    101
    >>> ht.bins[1].value
    'one oh one'
    >>> ht.bins[2].key 
    102
    >>> ht.bins[2].value 
    'updated one oh two'
    >>> HashTableInsert(ht, 201, "two oh one")
    >>> ht.bins[1].value
    'one oh one'
    >>> ht.bins[1].next.key
    201
    >>> ht.bins[1].next.value
    'two oh one'
    """
    hash_value = HashFunction(key, htable.size)
    
    if htable.bins[hash_value] is None:
        # Case 1: Bin is empty, create a new ListNode as the head
        htable.bins[hash_value] = ListNode(key, value)
    else:
        # Case 2: Bin is not empty, handle chaining
        current = htable.bins[hash_value]
        while current:
            if current.key == key:
                # Case 3: Key already exists, update the value
                current.value = value
                return
            if current.next is None:
                # Case 4: End of the linked list, add new ListNode
                current.next = ListNode(key, value)
                return
            current = current.next

def HashTableLookup(ht, key):
    """ HashTableLookup returns the value of the associated key if it
    appears in the hashtable ht. Return None if the key is not present.
    1) first compute the hash_value for the key
    2) check if the associated bin is empty and if so return None
    3) if bin is not empty use a loop to check if key exists in table
    4) if the key is present return the associated value, else return None.
    >>> ht = HashTable(10)
    >>> HashTableInsert(ht, 101, "one oh one")
    >>> HashTableInsert(ht, 102, "one oh two")
    >>> HashTableInsert(ht, 102, "updated one oh two")
    >>> HashTableInsert(ht, 201, "two oh one")
    >>> HashTableLookup(ht, 101)
    'one oh one'
    >>> HashTableLookup(ht, 102)
    'updated one oh two'
    >>> HashTableLookup(ht, 201)
    'two oh one'
    >>> HashTableLookup(ht, 202) == None
    True
    """
    hash_value = HashFunction(key, ht.size)
    
    if ht.bins[hash_value] is None:
        return None  # Case 1: Bin is empty, key is not present
    
    # Case 2: Bin is not empty, search through the linked list
    current = ht.bins[hash_value]
    while current:
        if current.key == key:
            return current.value  # Key found, return the associated value
        current = current.next
    
    return None  # Key not found


#RQ4
def password_checker(passwords, queries):
    """
    password_checker() takes a list of passwords and a list of queries and 
    outputs a list of booleans T/F indicating which of the queries matches
    any of the passwords. Your solution should use a HashTable of size 100000.
    
    >>> password_checker(['A6','B7','X15'], ['A5', 'A6', 'B7', 'B8', 'X15', 'X14'])
    [False, True, True, False, True, False]
   
    >>> password_checker(['#A60','?B7','!X15!'], ['#A5', '#A60', '?B7', '?B8', '!X1#!', '@X14#'])
    [False, True, True, False, False, False]

    """
    ht = HashTable(100000)
    
    # Insert passwords into the hash table, converting them to integers
    for idx, password in enumerate(passwords):
        HashTableInsert(ht, idx, password)  # Use idx as the key and password as the value
    
    results = []
    # Check each query against the hash table
    for query in queries:
        found = False
        for key in range(len(passwords)):
            if HashTableLookup(ht, key) == query:
                results.append(True)
                found = True
                break
        if not found:
            results.append(False)
    
    return results  
    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
