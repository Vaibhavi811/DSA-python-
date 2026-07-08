# Finding out unique elements from array of duplicates
names=["Belly", "Conrad","Belly","Jeremiah","Jeremiah"]

def remove_duplicates(names):
    names.sort()
    left=0

    for right in range(1,len(names)):
        if names[left]!= names[right]:
            left+=1
            names[left]=names[right]
    
    return left+1

count= remove_duplicates(names)
print("Unique names:",count)