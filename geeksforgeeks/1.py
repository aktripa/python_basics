# Python program to interchange first and last elements in a lists

lst = [12,35,9,56,24]

def swapList(newList):
    listSize = len(newList)

    temp = newList[0]
    newList[0] = newList[listSize - 1]
    newList[listSize - 1] = temp

    return newList
print(swapList(lst))
