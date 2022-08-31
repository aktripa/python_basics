# create fibonacci series using recursion

def recr_fib(n):
    if n <= 1:
        return n
    else:
        return (recr_fib(n-1) + recr_fib(n-2))


n  = 10

for i in range(n):
    print(recr_fib(i))