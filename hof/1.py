def multiply_by_2(item):
    return item*2

x = list(map(lambda item:item*2 , [1,2,3]))    
    
# print(map(multiply_by_2, [1,2,3]))

# List Sorting

a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key=lambda x:x[1])

print(a)

lst = [i[0] for i in a]
print(lst)
