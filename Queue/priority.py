import heapq

Hospital=[]

# Insertion
heapq.heappush(Hospital,(2,"High Fever"))
heapq.heappush(Hospital,(3,"Fracture"))
heapq.heappush(Hospital,(1,"Heart Attack"))

# Display
print(Hospital)

# Deletion
heapq.heappop(Hospital)

print(Hospital)