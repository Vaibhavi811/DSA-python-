queue=[]

# Insertion
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

# Deletion
print("Deleted element:",queue.pop(0))

# IsEmpty?
print("Is queue empty?",len(queue)==0)

# Display
print("Queue:",queue)