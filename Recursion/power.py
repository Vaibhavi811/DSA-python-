# Power of a number using recursion
def power(num,p):
    if p==0:
        return 1
    else:
        return num * power(num,p-1)
    
print(power(2,3))