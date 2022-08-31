from operator import length_hint
 
# Initializing list
test_list = [ 1, 4, 5, 7, 8 ]

list_len = len(test_list)

list_len_hint = length_hint(test_list)

print(list_len_hint)