# Print numbers from 1 to n using recursion
def print_no(num):
    if num==1:
        print(1,end=" ")
        return
    else:
        print_no(num-1)
        print(num,end=" ")

print_no(8)