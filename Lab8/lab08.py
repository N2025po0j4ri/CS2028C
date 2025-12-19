## Lab 8: Grids ##


_author_ = "Nirupama Poojari"
_credits_ = ["Your list of helpers"]
_email_ = "poojarna@mail.uc.edu" # Your email address

''' For this assignment you will modify the following code so that you can experimentally test
the effectiveness of the function GridSearchExpanding, which was covered in the Module lecture. 
Your code should count the number of comparisons made to potential nearest points. 
That is, you will add code to count the number of comparisons made during the search.
We will expect to see that an improvement in the number of comparisons made using GridSearchExpanding function.
'''

# RQ - Below is the code for the test1() function, used to check your code answers.

def test1():
    g = Grid(200,200,-100.0,100.0,-100.0,100.0)
    for i in range(70,100):
        for j in range(70,100):
            GridInsert(g, i *(1.01), j * (1.012))
            GridInsert(g, i *(1.11), j * (1.12))
 
    #RQ1
    point, dist, num_compares = GridLinearScanNN(g, -100.0,-100.0)
    print(point.x, point.y ,dist, num_compares)
    print (1, point.x == 70.7,point.y==70.84)
    print(2, abs(dist-241.5052) < 1e-3)
    print(3, num_compares == 3)
    
    #RQ2
    point, dist, num_compares = GridLinearScanNN(g, 100.0,100.0)
    print(point.x, point.y ,dist, num_compares)
    print (1, point.x == 99.9 ,point.y==99.68)
    print(2, abs(dist-0.3352) < 1e-3)
    print(3, num_compares == 312)
    #RQ3
    point, dist, num_compares = GridSearchExpanding(g, -100.0,-100.0)
    print(point.x, point.y ,dist, num_compares)
    print (1, point.x == 70.7,point.y==70.84)
    print(2, abs(dist-241.5052) < 1e-3)
    print(3, num_compares == 3) 
    #RQ4
    point, dist, num_compares = GridSearchExpanding(g, 100.0, 100.0)
    print(point.x, point.y ,dist, num_compares)
    print (1, point.x == 99.9 , point.y == 99.68)
    print(2, abs(dist-0.3352) < 1e-3)
    print(3, num_compares == 2)

    
 # Starter Code  
import math
    
class Grid():
    def __init__(self, num_x_bins, num_y_bins, x_start, x_end, y_start, y_end):
        self.num_x_bins = num_x_bins
        self.num_y_bins = num_y_bins
        self.x_start = x_start 
        self.x_end = x_end 
        self.y_start = y_start
        self.y_end = y_end
        self.x_bin_width = (x_end - x_start) / num_x_bins
        self.y_bin_width = (y_end - y_start) / num_y_bins
        self.bins =  [[None for _ in range(num_y_bins)] for _ in range(num_x_bins)]
    

class GridPoint():
    def __init__(self, x,y,next=None):
        self.x = x
        self.y = y
        self.next = next


def GridInsert(g, x, y):
    xbin = int((x - g.x_start) / g.x_bin_width)
    ybin = int((y - g.y_start) / g.y_bin_width)
 
    # Check that the point is within the grid.
    if (xbin < 0) or (xbin >= g.num_x_bins):
        return False
    if (ybin < 0) or (ybin >= g.num_y_bins):
        return False
    
    # Add the point to the front of the list. 
    next_point = g.bins[xbin][ybin]
    g.bins[xbin][ybin] = GridPoint(x, y)
    g.bins[xbin][ybin].next = next_point
    return True

def MinDistToBin(g, xbin, ybin, x, y):
    '''The function returns the minimum distance of the bin
with indices (xbin,ybin) from the point (x,y). We start by
checking that the bin indices are valid. We use an infinite
distance (math.inf) to indicate that the function’s caller has
referenced an invalid bin. '''
    # Check that the bin is valid.
    if (xbin < 0) or  (xbin >= g.num_x_bins):
        return math.inf
    if (ybin < 0) or (ybin >= g.num_y_bins):
        return math.inf

    x_min = g.x_start + xbin * g.x_bin_width
    x_max = g.x_start + (xbin + 1) * g.x_bin_width
    x_dist = 0
    if  x < x_min:
        x_dist = x_min - x
    if  x > x_max:
        x_dist = x - x_max

    y_min = g.y_start + ybin * g.y_bin_width
    y_max = g.y_start + (ybin + 1) * g.y_bin_width
    y_dist = 0
    if y < y_min:
      y_dist = y_min - y
    if y > y_max:
      y_dist = y - y_max
    return math.sqrt(x_dist*x_dist + y_dist*y_dist)

def GridLinearScanNN(g, x, y): 
    ''' The function returns the nearest point to target (x,y). 
We return both the point and its distance as a tuple.You are to add logic to 
return the number of comparisons. We start by initializing the variables for 
best_candidate and best_distance. The nested for-loops allow us generate index
pairs to check every possible bin. A bin is searched only if it satisfies the
MinDistToBin check. Using the Euclidean distance, we check if any point
in the linked list of points within the bin is closer than the best_candidate seen so far.
'''
    num_compares = 0  # Initialize comparison counter
    best_dist = math.inf
    best_candidate = None

    for xbin in range(g.num_x_bins):
        for ybin in range(g.num_y_bins):
            if MinDistToBin(g, xbin, ybin, x, y) < best_dist:
                current = g.bins[xbin][ybin]
                while current != None:
                    num_compares += 1  # Increment comparison count
                    dist = math.sqrt((x - current.x)**2 + (y - current.y)**2)
                    
                    if dist < best_dist:
                        best_dist = dist
                        best_candidate = current
                    current = current.next
    return best_candidate, best_dist, num_compares

def GridCheckBin(g,xbin,ybin, x, y, threshold): 
    '''The function returns the nearest point within a single bin indexed by (xbin,ybin)
    to target (x,y), which is closer than some threshold distance.
'''
    num_compares = 0  # Initialize comparison counter
    if (xbin < 0) or (xbin >= g.num_x_bins):
        return None, num_compares
    if (ybin < 0) or (ybin >= g.num_y_bins):
        return None, num_compares

    best_candidate = None
    best_dist = threshold

    current = g.bins[xbin][ybin]
    while current != None:
        num_compares += 1  # Increment comparison count
        dist = math.sqrt((x - current.x)**2 + (y - current.y)**2)
        
        if dist < best_dist:
            best_dist = dist
            best_candidate = current
        current = current.next
    return best_candidate, num_compares


def GridSearchExpanding(g, x, y):
    ''' The function finds the nearest neighbor to (x,y) in the grid g. It works by
prioritizing the order of the bins to search by using the distance of the bin to the point.
We start by finding the bin that contains (x,y) or the nearest bin, if no bin contains it. 
We use the pair (xb,yb) to denote this initial bin to check for
the best candidate point. '''
    num_compares = 0  # Initialize comparison counter
    best_d = math.inf
    best_pt = None

    xb = int((x - g.x_start) / g.x_bin_width)
    if xb < 0: xb = 0
    if xb >= g.num_x_bins:  xb = g.num_x_bins - 1

    yb = int((y - g.y_start) / g.y_bin_width)
    if yb < 0: yb = 0
    if yb >= g.num_y_bins: yb = g.num_y_bins - 1

    # Check the initial bin
    pt, n_c = GridCheckBin(g, xb, yb, x, y, best_d)
    num_compares += n_c  # Increment comparisons made
    if pt is not None:
        best_d = math.sqrt((x - pt.x) ** 2 + (y - pt.y) ** 2)
        best_pt = pt

    steps = 1
    explore = True
    while explore:
        explore = False
        xoff = -steps
        while xoff <= steps:
            yoff = steps - abs(xoff)
            if MinDistToBin(g, xb + xoff, yb - yoff, x, y) < best_d:
                pt, n_c = GridCheckBin(g, xb + xoff, yb - yoff, x, y, best_d)
                num_compares += n_c
                if pt is not None:
                    best_d = math.sqrt((x - pt.x) ** 2 + (y - pt.y) ** 2)
                    best_pt = pt
                explore = True

            if (MinDistToBin(g, xb + xoff, yb + yoff, x, y) < best_d) and (yoff != 0):
                pt, n_c = GridCheckBin(g, xb + xoff, yb + yoff, x, y, best_d)
                num_compares += n_c
                if pt is not None:
                    best_d = math.sqrt((x - pt.x) ** 2 + (y - pt.y) ** 2)
                    best_pt = pt
                explore = True
            xoff = xoff + 1

        steps = steps + 1
    
    return best_pt, best_d, num_compares



if __name__ == "__main__":
  test1()           
