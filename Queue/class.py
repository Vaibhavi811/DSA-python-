class Queue():
    def __init__(self):
        self.queue=[]

    def insert(self,items):
        self.queue.append(items)
        print("Inserted ",items)

    def IsEmpty(self):
        return len(self.queue)==0
    
    def delete(self):
        if self.IsEmpty():
            print("Error: Queue is empty.")
            return
        return self.queue.pop(0)
    
    def display(self):
        if self.IsEmpty():
            print("Error: Queue is empty.")
            return
        print("Queue:", self.queue)

q=Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)
q.insert(50)

q.display()

print("Is queue empty?", q.IsEmpty())
print("Deleted element:", q.delete())

q.display()