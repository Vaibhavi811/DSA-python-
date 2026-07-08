array=[1,2,3,4,5,6,7,8]

# method 1
for i in range(len(array)):
    print(array[i], end=" ")


print()


# Method 2
for i in array:
    print(i, end=" ")


print()

# Method 3
for i in range(len(array)-1,-1,-1):
    print(array[i], end=" ")

print()

# Method 4
for i in array[::-1]:
    print(i, end=" ")

print()

# Method 5
for i in reversed(array):
    print(i, end=" ")