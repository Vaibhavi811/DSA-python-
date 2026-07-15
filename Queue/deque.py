from collections import deque
q= deque()

# Insertion
q.append(10)
q.append(20)
q.append(30)
q.append(40)

print("Queue:",q)

# Isempty
print("Is queue empty?", len(q)==0)

# Deletion
print("Deleted elements:", q.popleft())

# Display
print("Queue:",q)