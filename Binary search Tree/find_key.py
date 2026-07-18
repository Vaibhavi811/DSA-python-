class node:
    def __init__(self,data):
        self.left= None
        self.data= data
        self.right= None

class Bst:
    def __init__(self):
        self.start= None

    def insert(self,item):
        if self.start is None:
            self.start= node(item)
            return
        
        ptr= self.start
        while True:
            if item>ptr.data:
                if ptr.right is None:
                    ptr.right= node(item)
                    return 
                ptr= ptr.right
            elif item<ptr.data:
                if ptr.left is None:
                    ptr.left= node(item)
                    return
                ptr= ptr.left

            else:
                print("ERROR: Duplicates Found.")
                return

    def display(self):
        if self.start is None:
            return
        
        queue=[self.start,None]
        while queue:
            value= queue.pop(0)

            if value is None:
                print()
                if queue:
                    queue.append(None)
                continue

            print(value.data,end="  ")
            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)

# Method 1
    def find_key(self,k):
        if self.start is None:
            return False
        
        ptr= self.start
        while True:
            if k>ptr.data:
                if ptr.right is None:
                    return False
                ptr= ptr.right

            elif k<ptr.data:
                if ptr.left is None:
                    return False
                ptr= ptr.left

            else:
                return True
            
# Method 2
    def find(self,key):
        if self.start is None:
            return False
        
        ptr= self.start
        while ptr:
            if ptr.data== key:
                return True
            elif key> ptr.data:
                ptr= ptr.right
            else:
                ptr= ptr.left
        return False
    
# Method 3
    def search(self,root,key):
        if root is None:
            return False
        if root.data== key:
            return True
        elif key> root.data:
           return self.search(root.right,key)
        else:
           return self.search( root.left,key)


t= Bst()
t.insert(8)
t.insert(27)
t.insert(17)
t.insert(26)
t.insert(5)
t.insert(11)

t.display()
print()

print("Does Tree contain 26?",t.find_key(26))
print("Does Tree contain 11?",t.find(11))
print(t.search(t.start,77))

