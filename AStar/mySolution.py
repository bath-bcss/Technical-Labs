import Base
import time
import math




def calcScore(grid, x, y):
    return grid.getAttr(x, y, "heuristic") + grid.getAttr(x, y, "distance")

#This takes in the position of the current cell and the end cell
#and uses it to calculate the heuristic
def calcHeuristic(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    '''
    return (dx + dy) #The manhattan distance
    return math.sqrt(dx * dx + dy * dy) #Euclidian distance
    '''
    return (min(dx, dy) * (1.41421 - 1) + max(dx, dy)) #This calculates the distance by moving diagonally towards the object until aligned then the straight line distance


#Sets the score of a cell
def setCellScore(grid, prevX, prevY, nextX, nextY):
    #-1 means the cell has never been visited before, this sets the heuristic as this is constant
    if(grid.getAttr(nextX, nextY, "score") == -1):
        estDistanceFromEnd = calcHeuristic(nextX, nextY, grid.endX, grid.endY) 
        grid.setAttr(nextX, nextY, "heuristic", estDistanceFromEnd)

    #Calculates the distance and score to that node   
    if(grid.getAttr(nextX, nextY, "score") > calcScore(grid, nextX, nextY) or grid.getAttr(nextX, nextY, "score") == -1):
        grid.setAttr(nextX, nextY, "distance", grid.getAttr(prevX, prevY, "distance") + math.dist([prevX, prevY], [nextX, nextY]))

        grid.setAttr(nextX, nextY, "score", calcScore(grid, nextX, nextY))

        grid.setBack(nextX, nextY, nextX - prevX, nextY - prevY)

#Adds neighbouring nodes to the given node
def addNeighbours(grid, opList, cx, cy):
    for x in range(-1, 2):
        for y in range(-1, 2):
            #Adds nodes in a 3 by 3 grid around the given node (apart from when x and y are 0 as that is just the given node)
            if((x != 0 or y != 0) and cx + x >= 0 and cx + x < grid.width and 
            cy + y >= 0 and cy + y < grid.height and 
            grid.getKey(cx + x, cy + y) != "#" and grid.isCellOpen(cx + x, cy + y)
            and not grid.cellInQueue(cx + x, cy + y)):

                setCellScore(grid, cx, cy, cx + x, cy + y)
                opList.add(cx + x, cy + y, grid)
                grid.setCellInQueue(cx + x, cy + y)

def printPath(grid):
    print("----")
    cx = grid.endX
    cy = grid.endY

    path = []
    path.append([cx, cy])
    while(cx != grid.startX or cy != grid.startY):
        nx = cx - grid.getBackX(cx, cy)
        ny = cy - grid.getBackY(cx, cy)
        cx = nx
        cy = ny
        path.append([cx, cy])

    for i in range(len(path)):
        print(path[len(path) - i - 1])
        grid.setCellAsPath(path[len(path) - i - 1][0], path[len(path) - i - 1][1])
    
    grid.printGrid()

def findShortestPath():
    grid = Base.Grid("map3.txt", { "score": -1, "distance": -1, "heuristic": -1 })#Load map

    grid.printGrid()#Show map

    currentX = grid.startX
    currentY = grid.startY
    opList = Base.Heap(100)
    #opList = Base.PriorityQueue()
    run = True

    #Set start node value
    grid.setAttr(currentX, currentY, "score", 0)
    grid.setAttr(currentX, currentY, "distance", 0)
    grid.setAttr(currentX, currentY, "heuristic", 0)
    grid.closeCell(currentX, currentY)
    
    addNeighbours(grid, opList, currentX, currentY)

    

    while(opList.length() > 0):#While there are still possible routes
        nextCell = opList.pop(grid)#Gets the node most likely to lead you to the end
        currentX = nextCell.x
        currentY = nextCell.y

        #Have we found the end
        if(currentX == grid.endX and currentY == grid.endY):
            printPath(grid)
            return

        #print(currentX, currentY)

        #Close the cell so it cannot be visited again
        grid.closeCell(currentX, currentY)

        #Add neighbouring nodes to open list
        addNeighbours(grid, opList, currentX, currentY) 
    
    
startTime = time.time()
findShortestPath()

print("Found path in:", time.time() - startTime)