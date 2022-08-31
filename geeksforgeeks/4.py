# Python - swap elements in String List

test_list = ['Gfg','is','best','for','Geeks']

print('The Original list : ' + str(test_list))

res = [sub.replace('G','g').replace('e','G') for sub in test_list]

print(res)