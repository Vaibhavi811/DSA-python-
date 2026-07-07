# Time complexity-- O(log n)
list1=[1,3,4,5,6,8,11]
target= 8

def Binary_Search(target, list1):
    low=0
    high=len(list1)-1

    while(low<=high):
        middle= (low+high)//2

        if(target==list1[middle]):
            return middle
        elif(target<list1[middle]):
            high= middle-1
        else:
            low= middle+1

    return -1

result= Binary_Search(target, list1)

if (result!=-1):
     print("Found at:",result)
else:
    print("NOT FOUND")