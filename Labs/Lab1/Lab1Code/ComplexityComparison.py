import random
import time
def basicSearch(value, arr, n):
    for i in range(n):
        if(arr[i] == value):
            return i

    return -1

def binarySearch(value, arr, n):
    lower = 0
    upper = n - 1
    while upper - lower > 0:
        mid = int((upper + lower) / 2)
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            lower = mid + 1
        else:
            upper = mid - 1
    
    return upper


def bubbleSort(arr, n):
    for i in range(n):
        for j in range(n - i - 1):
            if(arr[j] > arr[j+1]):
                swap = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = swap
    return arr

def test1():
    a = []
    n = 1000000
    for i in range(n):
        a.append(i)

     
    #Generate an array of numbers that is n long and in order from smallest to largest
    startTime = time.time()
    for i in range(100):
        value = a[int(random.random() * n)]

        basicSearch(value, a, n)

    print("Linear search average time: " + str((time.time() - startTime)/100) + " Seconds per search")

    startTime = time.time()
    for i in range(100):
        value = a[int(random.random() * n)]

        binarySearch(value, a, n)
    
    print("Binary search average time: " + str((time.time() - startTime)/100) + " Seconds per search")


test1()
