# Python program to swap two elements in a list

lst = [1,2,3,4,5,6]

pos1 = 1
pos2 = 4


def swapPositions(lst,pos1,pos2):
    lst[pos1], lst[pos2] = lst[pos2] , lst[pos1]
    return lst

print(swapPositions(lst, pos1, pos2))