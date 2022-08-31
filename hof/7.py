#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]


lst = list(zip(my_strings,my_numbers))

lst.sort(key=lambda x: x[1])

sorted_list = [i[1] for i in lst]

print(sorted_list)