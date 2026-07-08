numbers=[1,2,3,4,5,6]

def two_pointer(numbers,sum):
    right= len(numbers)-1
    left=0
    while(left<right):
        if numbers[left]+ numbers[right]<sum:
            left+=1
        elif numbers[left]+ numbers[right]>sum:
            right-=1
        else:
            return left,right
        
    return -1,-1

l,r= two_pointer(numbers,8)
if(l!=-1 and r!=-1):
    print("Found at:",l,"and",r)
else:
    print("Not found.")

