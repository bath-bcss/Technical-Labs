def sumOfN(n):
    return n*(n + 1) / 2

def main():
    line = input().split()
    M = int(line[0])
    N = int(line[1])

    rows = []
    line = input().split()
    for i in range(M):
        rows.append(int(line[i]))

    rows.sort(reverse=True)

    money = 0
    equalNum = 1
    index = 0
    while N > 0:
        if N >= equalNum * (rows[index] - rows[index + 1]):
            money += equalNum * ( sumOfN(rows[index]) - sumOfN(rows[index + 1]) )
            N -= equalNum * (rows[index] - rows[index + 1])
            index += 1
            equalNum += 1
        else:
            money += N * ( sumOfN(rows[index]) - sumOfN(rows[index + 1]) )
            N -= N * (rows[index] - rows[index + 1])

    print(int(money))

main()