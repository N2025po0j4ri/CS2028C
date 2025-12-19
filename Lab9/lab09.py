# Module 9 - Required Questions - Spatial Trees

_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address

#RQ1 Compute a bounding box from a list of pairs representing 2D points

def ComputeBoundingBox(list_of_points):
    """ This function computes the smallest bounding box around a 2D
    list of points. The function returns a 2-tuple with ([xmin,xmax],[ymin,ymax])
     
    >>> ComputeBoundingBox([(1,2),(2,5),(-1,-4)])
    ([-1, 2], [-4, 5])
    >>> ComputeBoundingBox([(101,22),(201,501),(-1,-9),(-101,-400)])
    ([-101, 201], [-400, 501])
    """
    # Your Code Here
    if not list_of_points:
        return ([], [])

    # Initialize with the coordinates of the first point
    xmin = xmax = list_of_points[0][0]
    ymin = ymax = list_of_points[0][1]

    # Iterate through the list of points to find min and max values
    for point in list_of_points:
        x, y = point
        if x < xmin:
            xmin = x
        elif x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        elif y > ymax:
            ymax = y

    # Return the bounding box as a 2-tuple of lists
    return ([xmin, xmax], [ymin, ymax])
        

#RQ2 Write a function that takes a QuadTreeNode and x,y coordinates and inserts the point at the node.
# Your function QuadTreeNodeInsert(qtreenode, x, y) 
# should invoke a partition of the region if there are 4 or more points in a region.  
 
class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

class QuadTreeNode():
    def __init__(self,x_min=-1.,x_max=1.,y_min=-1.,y_max=1.):
        self.is_leaf = True
        self.num_points = 0
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.children  = [[None for _ in [0,1]] for _ in[0,1]]
        self.points =[]

class QuadTree():
   def __init__(self,root=None):
        self.root = root
        
def is_point_in_node(node, point):
    """ Helper function to check if a point is within the bounds of a node. """
    return (node.x_min <= point.x <= node.x_max and
            node.y_min <= point.y <= node.y_max)

def partition_node(node):
    """ Helper function to partition a node into four child nodes. """
    x_mid = (node.x_min + node.x_max) / 2.0
    y_mid = (node.y_min + node.y_max) / 2.0
    
    # Create child nodes
    node.children[0][0] = QuadTreeNode(node.x_min, x_mid, node.y_min, y_mid)
    node.children[0][1] = QuadTreeNode(node.x_min, x_mid, y_mid, node.y_max)
    node.children[1][0] = QuadTreeNode(x_mid, node.x_max, node.y_min, y_mid)
    node.children[1][1] = QuadTreeNode(x_mid, node.x_max, y_mid, node.y_max)
    
    # Move existing points to appropriate child nodes
    for p in node.points:
        for i in range(2):
            for j in range(2):
                if is_point_in_node(node.children[i][j], p):
                    node.children[i][j].points.append(p)
                    node.children[i][j].num_points += 1
    
    # Clear current node's points
    node.points = []
    node.num_points = 0
    node.is_leaf = False

def QuadTreeNodeInsert(node, x, y):
    """
    >>> r=QuadTreeNode(-1.0,1.0,-1.0,1.0)
    >>> q=QuadTree(r)
    >>> QuadTreeNodeInsert(q.root, 0.1,0.1)
    >>> q.root.num_points,q.root.is_leaf
    (1, True)
    >>> QuadTreeNodeInsert(q.root, 0.2,0.2)
    >>> QuadTreeNodeInsert(q.root, 0.3,0.3)
    >>> q.root.num_points
    3
    >>> QuadTreeNodeInsert(q.root,-0.6,-0.6)
    >>> q.root.num_points
    0
    >>> q.root.children[0][0].num_points
    1
    >>> q.root.children[1][1].num_points
    3
    >>> QuadTreeNodeInsert(q.root, 0.7, 0.7)
    >>> q.root.children[1][1].children[1][1].num_points
    1
    >>> q.root.children[1][1].children[0][0].num_points
    3
    
    """ # Your code for RQ2 Here
    point = Point(x, y)
    
    # 1. Determine into which child bin the point should go.
    if not is_point_in_node(node, point):
        return
    
    # 2. Add the point to the correct child (recursively) if node is not leaf.
    if not node.is_leaf:
        for i in range(2):
            for j in range(2):
                if is_point_in_node(node.children[i][j], point):
                    QuadTreeNodeInsert(node.children[i][j], x, y)
                    return
    
    # 3. Otherwise add point to leaf node
    node.points.append(point)
    node.num_points += 1
    
    # 4. Check whether there are 4 or more points at leaf node. If so split it.
    if node.num_points >= 4 and node.is_leaf:
        partition_node(node)

# 1.  Determine into which child bin the point should go.
# 2.  Add the point to the correct child (recursively) if node is not leaf.
# 3.  Otherwise add point to leaf node
# 4. Check whether there are 4 or more points at leaf node. If so split it by
# setting node.is_leaf to False, and calling QuadTreeNodeInsert for each point in node.points.
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
