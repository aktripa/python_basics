# Python program to interchange first and last elements in a lists

def swapList(newlist):
    newlist[0] , newlist[-1]  = newlist[-1] , newlist[0]

    return newlist

    