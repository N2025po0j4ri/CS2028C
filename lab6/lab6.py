# CS2028 Lab 06 - Required Questions

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address


## Mod 6 Required Questions: Tries ##

""" Here is starter code for the specification of a Trie data structure"""
class TrieNode():
    def __init__(self,char,is_entry):
        self.char = char
        self.is_entry = True
        self.children = 26*[None]
    

class Trie():
    def __init__(self, root = None):
        self.root = TrieNode("",False)
        
def letter_index(ch):
    return ord(ch) - ord('A')

def trie_node_search(current: TrieNode, target: str, index : int):
    if index == len(target):
        if current.is_entry:
            return current
        else:
            return None

    next_letter = target[index]
    next_index = letter_index(next_letter)
    next_child = current.children[next_index]
    if next_child == None:
        return None
    else:
        return trie_node_search(next_child, target, index+1)



def trie_node_insert(current : TrieNode, new_value: str, index: int):
    if index == len(new_value):
        current.is_entry = True
    else:
        next_letter = new_value[index]
        next_index = letter_index(next_letter)
        next_child = current.children[next_index]
        if next_child == None:
            current.children[next_index] = TrieNode(next_letter,False)
            trie_node_insert(current.children[next_index], 
                           new_value, index + 1)
        else:
            trie_node_insert(next_child, new_value, index + 1)
            



#RQ1 Using the starter code. Write a wrapper function that insert a string into a Trie

def insert(trie, word):
        """Insert a word into the trie
        >>> t = Trie(); insert(t,"HELLO"); insert(t,"HALLO")
        >>> t.root.char
        ''
        >>> t.root.children[7].char
        'H'
        >>> t.root.children[7].children[0].char
        'A'
        >>> t.root.children[7].children[4].char
        'E'
        """
        current = trie.root
        for letter in word:
            letter_index = ord(letter) - ord('A')
            if current.children[letter_index] is None:
                current.children[letter_index] = TrieNode(letter, False)
            current = current.children[letter_index]
        current.is_entry = True
        

#RQ2 
# Using the starter code. Write a wrapper function that searches for a string in a Trie.
# TrieSearch reports whether or not the target string was found in the trie.

def TrieSearch(trie , target):
    """ Doctests
    >>> t = Trie(); insert(t,"WAS"); insert(t,"WORD")
    >>> TrieSearch(t, "WH")
    'WH not found'
    >>> TrieSearch(t, "WAS")
    'WAS found'
    >>> TrieSearch(t, "WHERE") 
    'WHERE not found'
    >>> TrieSearch(t, "WORD")
    'WORD found'
    """
    current = trie.root
    for letter in target:
        letter_index = ord(letter) - ord('A')
        if current.children[letter_index] is None:
            return target + ' not found'
        current = current.children[letter_index]
    if current.is_entry:
        return target + ' found'
    else:
        return target + ' not found'


#RQ3 
# Write a function that takes a trie and a list of search words and 
# counts the number of words from the list that are present in the trie.

def count_words(trie, search_words):
    """ Doctests
    >>> t = Trie(); insert(t,"WAS"); insert(t,"WORD");insert(t,"HELLO"); insert(t,"HALLO")
    >>> count_words(t, ["WAS", "WORD", "HELLO", "HALLO"])
    4
    >>> count_words(t, ["NOWAS", "NOWORD", "NOHELLO", "NOHALLO"])
    0
    >>> count_words(t, ["NOWAS", "WAS" ,"WORD"])
    2
    """
    count = 0
    for word in search_words:
        current = trie.root
        found = True
        for letter in word:
            letter_index = ord(letter) - ord('A')
            if current.children[letter_index] is None:
                found = False
                break
            current = current.children[letter_index]
        if found and current.is_entry:
            count += 1
    return count

        

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
