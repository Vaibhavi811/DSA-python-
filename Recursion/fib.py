# Fibonacci Series -- 0 1 1 2 3 5 8...
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
    
for i in range(7):
    print(fib(i), end=" ")