# Time complexity-- O(1)
list1= [1,2,3,4,5,6]
target= 1

for i in range(len(list1)):
    if target== list1[i]:
        print("Found at", i)
        break

print("First element:",list1[0])