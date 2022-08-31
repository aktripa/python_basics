lst1 = ['a','b','c','d','e','f']

lst2 = [6,10,9,4,3,1]


lst_op = list(zip(lst1,lst2))

lst_op.sort(key=lambda y:y[1])

sorted_lst = [i[0] for i in lst_op]
print(sorted_lst)
