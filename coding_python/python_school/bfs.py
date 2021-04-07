from collections import deque


"""
William Ingersoll - 03/06/2021
ITSC-3153-002: Intro to Artificial Intelligence 

A program that uses depth first and breadth first search to manuever through a maze.


Note(s):
There are definitely some differences in my code and what my groupmates (or even you) have. I apologize if anything is hard to
make sense of, although I have ran through it to make sure it flows well.

The main thing I noticed was keeping many of the functions inside the node class instead of seperated, but I felt being able to reference self
instead of other variables from time to time was simpler, and I kind of just went on instinct on this project. 

Additionally I used the deque lib instead of making a queue via an array. I verified in class that this was alright, but if something dosen't work the
way you expect it to, or some of the lines of code don't read in a similiar way to others, I would wager that this is the reason.

That all being said, the project works from my end, and if you have any questions about my code, please email me at my school account and I would be
more than happy to clarify, it was a fun project and I look forward to more in the future.
"""


class grid:

    def __init__(self):
        self.grid = self.readGrid("grid.txt")

    # The grid values must be separated by spaces, e.g.
    # 1 1 1 1 1 
    # 1 0 0 0 1
    # 1 0 0 0 1
    # 1 1 1 1 1
    # Returns a 2D list of 1s and 0s
    def readGrid(self, filename):
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
    def outputGrid(self, grid, start, goal, path):
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
        #print('Exiting outputGrid')

class node:

    def __init__(self, values, parents):
        self.value = values
        self.parent = parents

    def printGrid(self, grid):
        for elem in grid:
            print(elem)

    def getNeighbors(self, location, grid):

        #setting an x and y point and initializing a list to hold the values
        loc = location
        x = loc[0]
        y = loc[1]
        locations = []
        
        #x and y are backwards dont worry about it
        #check all four adjacent locations on the grid, making sure they aren't a 1 and aren't out of bounds
        #if location satisfies this, we append it to the locations list
        if(grid[x+1][y] == 0 and x+1 > -1):
            locations.append([x+1, y])
        if(grid[x-1][y] == 0 and x-1 > -1):
            locations.append([x-1, y])    
        if(grid[x][y+1] == 0 and y+1 > -1):
            locations.append([x, y+1]) 
        if(grid[x][y-1] == 0 and y-1 > -1):
            locations.append([x, y-1]) 

        return locations

    def expandNode(self, grid, closed_list, open_list):
        #First we call the get neighbors function to get all our neighbors
        neighbors = self.getNeighbors(self.value, grid)
        #Initilize a list of future nodes and a list of neighbors to return
        new_nodes = []
        neighbor_list = []

        #For every neighbor, create a new node using that neighbor as the value, and the parent is set to the current node
        for elem in neighbors:
            new_nodes.append(node(elem, self))

        #Here we copy the queue so we can convert it into a regular list for ease of use
        open_list_copy = open_list.copy()
        closed_list_copy = closed_list.copy()
        temp_open = []
        temp_closed = []

        for elem in open_list:
            temp_open.append(open_list_copy.pop().value)
        for elem in closed_list:
            temp_closed.append(closed_list_copy.pop().value)


        #For every element in the list, we check if the value already exsists in either the open list or closed list
        #If the element is not present, we return it.
        for elem in new_nodes:
            if((elem.value in temp_closed) or (elem.value in temp_open)):
                pass
            else:
                neighbor_list.append(elem)
            
        return neighbor_list


def uniformedSearch(grid, start, goal, search_type):
    #First we setup our starting node, and our queues, appending current to the open list
    current = node(start, None)
    open_list = deque()
    closed_list = deque()
    open_list.append(current)
    found = False

    #Breadth-first search function 
    if(search_type=="bfs"):
        #Loop while there are elements remaining in the open list and we have not found the goal
        while(open_list and found == False):
            #We pop the left value for current to make this a queue
            current = open_list.popleft()
            #If the vurrent value is goal, then we stop the search because we found it.
            if(current.value == goal):
                found = True
            #If it is not the goal, then we add that to the closed list and expand node on it.
            closed_list.append(current)
            neighbor_list = (current.expandNode(grid, closed_list, open_list))
            #append the new nodes to the open list
            for neighbor in neighbor_list:
                open_list.append(neighbor)
    #Depth-first search function
    else:
        #Works the same as breadth first minus one difference
        while(open_list and found == False):
            #Instead of popping off the left side, we pop off of the right in order to make the queue a stack.
            #The module is called dequeue, but really it works for whatever structure you want, that way I only have to change this one thing
            current = open_list.pop()
            if(current.value == goal):
                found = True
            closed_list.append(current)
            neighbor_list = (current.expandNode(grid, closed_list, open_list))
            for neighbor in neighbor_list:
                open_list.append(neighbor)

    #Initilize the path, which is the solution to be passed to the prewritten code
    path = []
    #Append all of the closed list into the path
    for elem in closed_list:
        path.append(elem.value)
    #If the goal was not reachable, we should inform the user
    if(found==False):
        print("The goal could not be reached.")

    #Print requirements
    print("Length of Searched Nodes: " + str(len(closed_list)))
    print("Length of Unsearched Nodes: " + str(len(open_list)))
    return path


        
def main():
    #Initilize the grid, the user defined search method, the start, and the goal.
    bfs = grid()
    gr = bfs.readGrid("grid.txt")
    option = input("Type 'bfs' for breadth-first search, or type 'dfs' for depth-first-search: ")
    start = []
    goal = []
    start.append(int(input("Enter x value of starting position: ")))
    start.append(int(input("Enter y value of starting position: ")))
    goal.append(int(input("Enter x value of goal position: ")))
    goal.append(int(input("Enter y value of goal position: ")))

    #Run the uninformed search method and send it to the output grid function 
    path = uniformedSearch(gr, start, goal, option)
    bfs.outputGrid(gr, start, goal, path)
    

if __name__=="__main__":
    main()    
