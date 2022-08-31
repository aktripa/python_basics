from functools import reduce
scores = [73, 20, 65, 19, 76, 100, 88]
my_numbers = [5,4,3,2,1]

def accumulator(acc,item):
    return acc + item

print(reduce(accumulator , (my_numbers + scores)))