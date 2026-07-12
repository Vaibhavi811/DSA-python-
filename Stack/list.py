stack=[]

# pushing elements
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

# Popping
print("Deleted:",stack.pop())

# Peek
print("Last element:", stack[-1])

# IsEmpty?
print("Is List Empty?",len(stack)==0)

# Display
print("Stack[Top-->Bottom]",stack[::-1])