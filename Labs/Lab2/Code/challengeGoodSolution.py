class Heap:
    def __init__(self, length):
        self.data = [0] * length
        self.currentLength = 0
    
    def push(self, val):
        pos = self.currentLength + 1
        self.currentLength += 1

        while pos != 1 and self.data[int(pos / 2) - 1] < val:
            self.data[pos - 1] = self.data[int(pos / 2) - 1]
            pos = int(pos / 2)
        
        self.data[pos - 1] = val

    def pop(self):
        returnValue = self.data[0]
        self.currentLength -= 1
        self.data[0] = self.data[self.currentLength]

        pos = 1
        while pos * 2 < self.currentLength + 1:
            if self.data[pos * 2 - 1] > self.data[pos * 2]:
                child = pos * 2 
            else:
                child = pos * 2 + 1
            
            if self.data[pos - 1] < self.data[child - 1]:
                swap = self.data[pos - 1]
                self.data[pos - 1] = self.data[child - 1]
                self.data[child - 1] = swap
                pos = child
            else:
                break
        
        return returnValue



def main():
    line = input().split()
    M = int(line[0])
    N = int(line[1])

    pQ = Heap(10)
    line = input().split()
    for i in range(M):
        pQ.push(int(line[i]))

    totalMoney = 0
    for i in range(N):
        nextVal = pQ.pop()
        totalMoney += nextVal
        pQ.push(nextVal - 1)

    print(totalMoney)

main()