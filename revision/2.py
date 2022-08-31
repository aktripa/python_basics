# Python – Swap elements in String list

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

lst = [i.replace('G','e').replace('f','F').replace('e','E') for i in test_list]

print(lst)