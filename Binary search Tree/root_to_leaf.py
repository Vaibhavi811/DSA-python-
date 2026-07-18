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
        
        queue= [self.start,None]

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

    def printpath(self, queue):
        for i in range(len(queue)):
            print(queue[i].data,end=" ")
        print()

    def root_to_leaf(self, root,queue):
        if root is None:
            return
        
        queue.append(root)

        if root.left is None and root.right is None:
            self.printpath(queue)

        else:
            self.root_to_leaf(root.left, queue)
            self.root_to_leaf(root.right,queue)

        queue.pop()

t= Bst()
t.insert(8)
t.insert(5)
t.insert(17)
t.insert(26)
t.insert(6)
t.insert(11)

t.display()

queue=[]

print("Root to Leaf:")
t.root_to_leaf(t.start,queue)
