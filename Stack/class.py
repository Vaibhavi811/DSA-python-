class Stack():
    def __init__(self):
        self.lst=[]

    def push(self,items):
        self.lst.append(items)
        print("Inserted",items)

    def IsEmpty(self):
        return len(self.lst)==0
    
    def pop(self):
        if self.IsEmpty():
            print("Error: List is empty")
            return
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]
    
    def display(self):
        if self.IsEmpty():
            print("Error: List is empty")
            return
        print(self.lst)

S1= Stack()
S1.push(10)
S1.push(20)
S1.push(30)
S1.push(40)
S1.push(50)

print("IS stack empty?",S1.IsEmpty())
print("Deleted ",S1.pop())
print("Last element:",S1.peek())
S1.display()