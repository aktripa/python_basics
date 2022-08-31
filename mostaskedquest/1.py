# write a program to reverse a number

num = 1234567

lst = [i for i in str(num)]

lst.reverse()

rev_num = int(''.join(lst))

print(rev_num)
