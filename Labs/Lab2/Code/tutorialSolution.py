class Heap:
    def __init__(self, length):
        self.data = [0] * length
        self.currentLength = 0
    
    def push(self, val):
        pos = self.currentLength + 1 #index = pos - 1 
        self.currentLength += 1

        while pos != 1 and self.data[int(pos / 2) - 1] < val: #while not the root and the value is bigger than it parent
            self.data[pos - 1] = self.data[int(pos / 2) - 1] #move parent to child
            pos = int(pos / 2) #move pos up the tree
        
        self.data[pos - 1] = val #set the node equal to the value

    def pop(self):
        returnValue = self.data[0] #biggest value
        self.currentLength -= 1
        self.data[0] = self.data[self.currentLength] #move the node at the end of the tree to the root

        pos = 1 #start at root
        while pos * 2 < self.currentLength + 1: #while not going to go outside the tree
            if self.data[pos * 2 - 1] > self.data[pos * 2]: #get biggest child
                child = pos * 2 #set largest child index
            else:
                child = pos * 2 + 1
            
            if self.data[pos - 1] < self.data[child - 1]: #if the child is bigger than the parent then swap
                swap = self.data[pos - 1]
                self.data[pos - 1] = self.data[child - 1]
                self.data[child - 1] = swap
                pos = child
            else:
                break
        
        return returnValue

def main():
    n = int(input())
    h = Heap(1000000)
    line = input().split()
    for i in range(n):
        h.push(int(line[i]))

    m = int(input())
    for i in range(m):
        line = input().split()

        if line[0] == "1":
            h.push(int(line[1]))
        else:
            print(h.pop())


        



main()
