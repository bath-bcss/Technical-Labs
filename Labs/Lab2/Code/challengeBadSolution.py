class BasicQueue:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        val = max(self.data)
        self.data.remove(val)
        return val

line = input().split()
M = int(line[0])
N = int(line[1])

pQ = BasicQueue()
line = input().split()
for i in range(M):
    pQ.push(int(line[i]))

totalMoney = 0
for i in range(N):
    nextVal = pQ.pop()
    totalMoney += nextVal
    nextVal -= 1
    pQ.push(nextVal)

print(totalMoney)
