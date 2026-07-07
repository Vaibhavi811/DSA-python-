# Time complexity-- O(n^2)
list1= [1,2,3,3,2,1]

def find_duplicates(list1):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if(i!=j and list1[i]==list1[j]):
                return True
            
    return False

result= find_duplicates(list1)

if result:
    print("Duplicates found")
else:
    print("NO duplicates")