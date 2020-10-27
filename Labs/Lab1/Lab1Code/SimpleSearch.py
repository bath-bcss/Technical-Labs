import random
a = []

for i in range(100000):
    a.append(int(random.random() * 10000000))



def findValueIndex(val, arr):
    for i in range(len(arr)):
        if(val == arr[i]):
            return i

    return -1


valueToFind = a[int(random.random() * len(a))]
print("Find value: ", valueToFind)
#print("Array of random values: ", a)
print("Value at index: ", findValueIndex(valueToFind, a))


