# Time complexity-- O(n)
list1= [1,2,8,4,5,6,8]
target= 8

for i in range(len(list1)):
    if target== list1[i]:
        print("Found at:",i)
        