# CS2028 Lab 05 - Required Questions

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address

## Module 5: Required Questions - Binary Search Trees  ##

""" Here is a specification for BST Data Structure"""

class TreeNode():
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right =  None
        self.parent = None
                
class BinarySearchTree():
    def __init__(self):
        self.root = None

def insert_tree_node(tree, new_value):
    if tree.root == None:
        tree.root = TreeNode(new_value)
    else:
        insert_node(tree.root, new_value)
        
def insert_node(current_node, new_value):
    if new_value == current_node.value:
      print("Duplicate insert")
    if new_value < current_node.value:
        if current_node.left != None:
            insert_node(current_node.left, new_value)
        else:
            current_node.left = TreeNode(new_value)
            current_node.left.parent = current_node
    else:
        if current_node.right != None:
            insert_node(current_node.right, new_value)
        else:
            current_node.right = TreeNode(new_value)
            current_node.right.parent = current_node

# RQ1
def convert_to_tree(a):
    """ Write a function that takes an array a as an argument and 
    returns the binary tree obtained by inserting each 
    element in the array in same order.
    >>> t = convert_to_tree(np.array([7,8,6,9,5]))
    >>> t.root.value
    7
    >>> t.root.left.value
    6
    >>> t.root.right.value
    8
    >>> t = convert_to_tree(np.array([5,6,7,8,9]))
    >>> t.root.value
    5
    >>> t.root.right.value
    6
    >>> t.root.right.right.value
    7
    """
    tree = BinarySearchTree()
    for value in a:
        insert_tree_node(tree, value)
    return tree
    
#RQ2    
def convert_to_balanced_tree(a):
    """
    Write a function that creates and returns a balanced binary search tree
    from a sorted array a as argument (see textbook Figure 5-14) 
    by recursively dividing the elements into smaller subsets. 
    At each level, choose the middle value to be the node at that level. 
    If there is an even number of elements, then use the first/left of the 
    two middle elements.
    >>> t = convert_to_balanced_tree(np.array([5,6,7,8,9,10,11]))
    >>> t.root.value
    8
    >>> t.root.left.value
    6
    >>> t.root.right.value
    10
    >>> t = convert_to_balanced_tree(np.array([5,6,7,8,9]))
    >>> t.root.value
    7
    >>> t.root.right.value
    8
    >>> t.root.right.right.value
    9
    >>> t.root.left.value
    5
    >>> t.root.left.right.value
    6
    """
    def build_balanced_tree(arr):
        if not arr:
            return None
        mid = (len(arr) - 1) // 2  # Adjusted calculation for even number of elements
        root = TreeNode(arr[mid])
        root.left = build_balanced_tree(arr[:mid])
        root.right = build_balanced_tree(arr[mid + 1:])
        return root

    sorted_arr = sorted(a)
    bst = BinarySearchTree()
    bst.root = build_balanced_tree(sorted_arr)
    return bst

#RQ3
def find_max(tree):
    """ 
    Return the largest value in a binary search tree.
    >>> t = BinarySearchTree()
    >>> insert_tree_node(t,5)
    >>> insert_tree_node(t,2)
    >>> insert_tree_node(t,7)
    >>> insert_tree_node(t,9)
    >>> insert_tree_node(t,1)
    >>> find_max(t)
    9
    """
    if tree.root is None:
        return None
    current = tree.root
    while current.right:
        current = current.right
    return current.value
#RQ4
def inorder_traversal(root_node):
    """
    Carry out an inorder traversal of a binary search tree which prints out all values 
    within the tree in ascending order.
    >>> t = convert_to_tree(np.array([7,8,6,9,5]))
    >>> inorder_traversal(t.root)
    5 6 7 8 9 
    """
    if root_node is None:
        return
    inorder_traversal(root_node.left)
    print(root_node.value, end=' ')
    inorder_traversal(root_node.right)
    
import numpy as np
if __name__ == "__main__":
   import doctest
   doctest.testmod(verbose=True)

