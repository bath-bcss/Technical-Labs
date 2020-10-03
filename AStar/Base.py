class Cell:
    def __init__(self, attr, key):
        self.attr = attr.copy()
        self.key = key
        self.isPath = False
        self.backX = 0
        self.backY = 0
        self.isClosed = False
        self.inQueue = False

    def getKey(self):
        if(self.isPath):
            return "+"
        elif(self.isClosed):
            return "/"
        
        return self.key

class Grid:
    def __init__(self, mapName, attrs):
        file = open(mapName, "r").read().split("\n")


        self.width = int(file[0])
        self.height = int(file[1])

        self.grid = []

        self.startX = -1
        self.startY = -1
        self.endX = -1
        self.endY = -1

        for x in range(self.width):
            self.grid.append([])
            for y in range(self.height):
                self.grid[x].append(Cell(attrs, file[y + 2][x]))
                if(file[y + 2][x] == "S"):
                    self.startX = x
                    self.startY = y
                elif(file[y + 2][x] == "E"):
                    self.endX = x
                    self.endY = y
                    
        

        

    
    def printGrid(self):
        for y in range(self.height):
            string = ""
            for x in range(self.width):
                string += self.grid[x][y].getKey()
            print(string)

    def setAttr(self, x, y, attr, value):
        self.grid[x][y].attr[attr] = value

    def getAttr(self, x, y, attr):
        return self.grid[x][y].attr[attr]

    def getKey(self, x, y):
        return self.grid[x][y].getKey()

    def isCellOpen(self, x, y):
        return not self.grid[x][y].isClosed
    
    def setCellAsPath(self, x, y):
        self.grid[x][y].isPath = True

    def getBackX(self, x, y):
        return self.grid[x][y].backX
        
    def getBackY(self, x, y):
        return self.grid[x][y].backY
    
    def setBack(self, x, y, vx, vy):
        self.grid[x][y].backX = vx
        self.grid[x][y].backY = vy

    def closeCell(self, x, y):
        self.grid[x][y].isClosed = True

    def cellInQueue(self, x, y):
        return self.grid[x][y].inQueue
    
    def setCellInQueue(self, x, y):
        self.grid[x][y].inQueue = True

class PriorityQueueIndex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PriorityQueue:
    def __init__(self):
        self.data = []

    def add(self, x, y, grid):
        cellScore = grid.getAttr(x, y, "score")
        if(len(self.data) == 0):
            self.data.append(PriorityQueueIndex(x, y))
            return

        i = 0
        while(i < len(self.data) and grid.getAttr(self.data[i].x, self.data[i].y, "score") <= cellScore):
            if(self.data[i].x == x and self.data[i].y == y):
                return
            i += 1

        
        self.data.insert(i, PriorityQueueIndex(x, y))

    def pop(self, grid):
        cell = self.data[0]
        self.data.pop(0)
        return cell

    def length(self):
        return len(self.data)



class Heap:
    def __init__(self, startSize):
        self.data = []
        for i in range(startSize):
            self.data.append(0)
        self.index = 1
        self.size = startSize

    def add(self, x, y, grid):
        cellScore = grid.getAttr(x, y, "score")
        #cellScore = grid

        if(self.index == self.size):
            for i in range(int(self.size * .5) + 1):
                self.data.append(0)
            self.size = len(self.data)

        i = int(self.index / 2)
        j = self.index

        while i > 0 and grid.getAttr(self.data[i - 1].x, self.data[i - 1].y, "score") >= cellScore:
            self.data[j - 1] = self.data[i - 1]
            j = i
            i = int(i / 2)

        self.data[j - 1] = PriorityQueueIndex(x, y)
        self.index += 1

    def adjust(self, grid):
        i = 1
        j = 2 * i
        node = self.data[i - 1]
        currentNodeScore = grid.getAttr(node.x, node.y, "score")

        while j <= self.index:
            nextNodeScore = grid.getAttr(self.data[j-1].x, self.data[j-1].y, "score")
            if j < self.index and nextNodeScore > grid.getAttr(self.data[j].x, self.data[j].y, "score"):
                j += 1
                grid.getAttr(self.data[j-1].x, self.data[j-1].y, "score")
            
            if currentNodeScore <= nextNodeScore:
                break
            else:
                self.data[int(j/2) - 1] = self.data[j - 1]
            
            j = 2 * j
        
        self.data[int(j/2) - 1] = node

    def pop(self, grid):
        if(self.index == 1):
            return 0/0
        elif(self.index == 2):
            self.index -= 1
            return self.data[0]
        
        returnValue = self.data[0]

        self.data[0] = self.data[self.index - 2]
        self.index -= 1

        self.adjust(grid)

        return returnValue


    def print(self, grid):
        for i in range(self.index - 1):
            print(self.data[i].x, self.data[i].y, grid.getAttr(self.data[i].x, self.data[i].y, "score"))
            #print(self.data[i])
        #print("-")

    def length(self):
        return self.index - 1


    