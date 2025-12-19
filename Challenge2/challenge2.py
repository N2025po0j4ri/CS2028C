# CS2028 Challenge 2 - Required Questions

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address

class TreeNode():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self):
        self.root = None

def insert_tree_node(tree, new_value):
    if tree.root is None:
        tree.root = TreeNode(new_value)
    else:
        insert_node(tree.root, new_value)
        
def insert_node(current_node, new_value):
    if new_value == current_node.value:
        print("Duplicate insert")
    if new_value < current_node.value:
        if current_node.left is not None:
            insert_node(current_node.left, new_value)
        else:
            current_node.left = TreeNode(new_value)
    else:
        if current_node.right is not None:
            insert_node(current_node.right, new_value)
        else:
            current_node.right = TreeNode(new_value)

def convert_to_tree(a):
    tree = BinarySearchTree()
    for value in a:
        insert_tree_node(tree, value)
    return tree.root

def compare(t1, t2):
    """
    >>> t1 = convert_to_tree(np.array([7,8,6,9,5]))
    >>> t2 = convert_to_tree(np.array([7,8,6,5,9]))
    >>> compare(t1, t2)
    True
    >>> t1 = convert_to_tree(np.array([7,8,6,9,5]))
    >>> t2 = convert_to_tree(np.array([7,8,5,6,9]))
    >>> compare(t1, t2)
    False
    >>> t1 = convert_to_tree(np.array([7,8,6,9,10,5,2]))
    >>> t2 = convert_to_tree(np.array([7,8,6,9,10,5,1]))
    >>> compare(t1, t2)
    False
    """
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    return (t1.value == t2.value and
            compare(t1.left, t2.left) and
            compare(t1.right, t2.right))
    
    return compare(t1, t2)

import numpy as np
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
