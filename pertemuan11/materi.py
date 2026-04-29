mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

if 4 in mylist:
    print("Found")

def linearSearch(array,targetVal):
    for i in range(len(array)):
        if array[i] == targetVal:
            return i
    return -1

x = 4
result = linearSearch(mylist, 4)
print(result)