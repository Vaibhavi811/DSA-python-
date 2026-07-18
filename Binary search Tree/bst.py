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

    def inorder(self,root):
        if root is None:
            return
        
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)


t= Bst()
t.insert(8)
t.insert(17)
t.insert(27)
t.insert(5)
t.insert(6)
t.insert(26)

t.display()

print()

print("Inorder:",end=" ")
t.inorder(t.start)


        

        