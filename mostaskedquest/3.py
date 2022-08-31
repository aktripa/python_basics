# Find pairs with given numbers in list

lst = [8,7,2,5,3,1]
k = 10
l = len(lst)

for i in range(l):
    for j in range(i+1,l):
        if lst[i] + lst[j] == k:
            print(lst[i],lst[j])