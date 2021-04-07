import heapq
import math

"""
Author: William Ingersoll

A program that uses informed search algorithims to determine a path through a maze


"""





# ---PROVIDED CODE--- #
# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1 
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of 1s and 0s
def readGrid(filename):
    #print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])
    
    f.close()
    #print 'Exiting readGrid'
    return grid
 
# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1 
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path):
    #print('In outputGrid')
    filenameStr = 'path.txt'
 
    # Open filename
    f = open(filenameStr, 'w')
 
    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'
 
    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path)-1:
            grid[p[0]][p[1]] = '*'
 
    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            
            # Don't add a ' ' at the end of a line
            if c < len(row)-1:
                f.write(str(col)+' ')
            else:
                f.write(str(col))
 
        # Don't add a '\n' after the last line
        if r < len(grid)-1:
            f.write("\n")
 
    # Close file
    f.close()
    # print('Exiting outputGrid')

# ---GROUP PRODUCED CODE--- #
class Node:
    def __init__(self, value, parent, fn, gn, hn):
        self.value = value
        self.parent = parent
        self.fn = fn
        self.gn = gn
        self.hn = hn
        
    def __lt__(self, other):
      return self.fn < other.fn
  
       
def get_neighbors(loc, grid):
        #setting an x and y point and initializing a list to hold the values
        x = loc[0]
        y = loc[1]
        neighbors = []
        
        
        #check all four adjacent neighbors on the grid, making sure they aren't a 0 and not out of bounds
        #if location satisfies this, we append it to the neighbors list
        if( (x+1 < len(grid)) and not(grid[x+1][y] == 0 )):
            neighbors.append([x+1, y])
        if( not(x-1 == -1) and not(grid[x-1][y] == 0 )):
            neighbors.append([x-1, y])
        if( (y+1 < len(grid)) and not(grid[x][y+1] == 0 )):
            neighbors.append([x, y+1])
        if( not(y-1 == -1) and not(grid[x][y-1] == 0 )):
            neighbors.append([x, y-1])

        return neighbors

#A function to find the euclidian distance between the expanded node and the goal 
def euclid(point_a, point_b):
    #calculate the difference between the x and y
    xdist = point_b[0] - point_a[0]
    ydist = point_b[1] - point_a[1]
    #square the two results and add them
    result = (math.pow(xdist, 2)) + (math.pow(ydist, 2))
    #Square root that result and return
    result = math.sqrt(result)
    return result

#Function that returns the value at a set of coordinates
def step_calc(point, grid):
  return (grid[point[0]][point[1]])

#The heavily edited expand node function, takes in two additional parameters:
#The first is greedy, which tells the function to set the path cost to 0 so it isn't calculated during greedy search
#The second is the goal coordinates, which is necessary for the heuristic function
def expand_node(node, grid, cList, oList, greedy, goal):
    nghbrs = get_neighbors(node.value, grid)

    #For each neighboring node
    for e in nghbrs:

        #First we calculate our heuristic
        distance = euclid(e, goal)
        #Then we get the step cost
        step_cost = step_calc(e, grid)
        #If we're greedy searching we don't need a path cost
        if(greedy):
            path_cost=0
        #Else we add the step cost to the current nodes path cost
        else:
            path_cost = node.gn+step_cost

        #Create a new node with all this info
        new_node = Node(e, node, (path_cost+distance), path_cost, distance)

        #Create a new openlist of the actual values, not just coordinates
        olist_values = []
        for elem in oList:
            olist_values.append(elem.value)
        
        #If the expanded node is in either closed list or openlist we pass, else we add it to openlist
        if((e in cList) or (e in olist_values)):
            pass
        else:
            heapq.heappush(oList, new_node)

    return oList
          
#The informed search algorithim, which is very similiar to the original uniformed search
def informedSearch(grid, start, goal, searchType):
    
    if searchType == "a*":
        openList = []
    
        closedList = [] # list of locations already searched
        
        current = Node(start, None, 0, 0, 0)
        goalReached = False
        path = []
        
        #The only thing different is that we use the heapq in order to store info, and print some additional info
        while not goalReached:
            if current.value == goal:
                path = setPath(current,[]) 
                print("Final Path: " + str(path))
                print("Goal Reached")
                break
            closedList.append(current.value)
            openList = expand_node(current,grid,closedList,openList, False, goal)
            if not(openList):
                print("Goal was not reached")
                break
            current = heapq.heappop(openList)

        print("# of States Expanded: " + str(len(closedList)))
        return path
    
    if searchType == "greedy":
        openList = []
    
        closedList = [] # list of locations already searched
        
        current = Node(start, None, 0, 0, 0)
        goalReached = False
        path = []

        while not goalReached:
            if current.value == goal:
                path = setPath(current,[]) 
                print(path)
                print("Goal was reached")
                break
            closedList.append(current.value)
            openList = expand_node(current,grid,closedList,openList, True, goal)
            if not(openList):
                print("Goal could not be reached")
                break
            current = heapq.heappop(openList)
        
        print("# of States Expanded: " + str(len(closedList)))
        return path

def setPath(goalNode, path):
    current = goalNode
    hasParent = True

    while hasParent:
        pos = current.value
        path.append(pos)
        if current.parent == None:
            hasParent = False
        else:
            current = current.parent

    return path


def main():
    # ---TEST--- #
    startLocationList = [7,1]
    goalLocationList = [1,8]
    test = readGrid('grid.txt')
    node = Node([1,0], [0,0], 0, 0, 0)
    clist = []
    olist = []


    search_type = input("Enter your preffered search type (a*/greedy): ")

    path = informedSearch(test,startLocationList,goalLocationList,search_type)

    print("Heuristic Function: Euclidian Distance")
    
    print("Outputting grid...")
    outputGrid(test,startLocationList,goalLocationList,path)


if __name__ == '__main__':
	main()
else:
	print('Our script is being imported as a module by some other python script')
