# Print numbers in reverse order using recursion upto 1
def rev_num(num):
    if num==1:
        print(1,end=" ")
        return
    else:
        print(num,end=" ")
        rev_num(num-1)

rev_num(8)

