# Array/list-- collection of related data stored in contiguous memory location.

array= [1,2,3,4]

# Adding elements
array.append(5)
array.append(6)
array.append(7)
array.append(9)
array.append(10)

array.insert(7,8)
print(array)

# Removing elements
array.pop()
array.pop(0)

print(array)

array.remove(5)
del array[2]

print(array)