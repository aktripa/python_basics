list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]


# o/p ['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']

lst = list(zip(list1,list2))

lst.sort(key=lambda y:y[1])

output = [i[0] for i in lst]
print(lst)
print(output)    