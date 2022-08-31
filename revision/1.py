# Python program to interchange first and last elements in a list

lst = [1,2,3,4,5,6]

t = lst[0]
k = lst[len(lst)-1]

lst[0],lst[len(lst)-1] = lst[len(lst)-1],lst[0]

print(lst)