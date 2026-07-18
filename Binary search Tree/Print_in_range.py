class node:
    def __init__(self,data):
        self.left= None
        self.data= data
        self.right= None

class bst():
    def __init__(self):
        self.start= None

    def insert(self,item):
        if self.start is None:
            self.start= node(item)
            return 

        ptr= self.start
        while True:
            if item> ptr.data:
                if ptr.right is None:
                    ptr.right= node(item)
                    return
                ptr= ptr.right

            elif item< ptr.data:
                if ptr.left is None:
                    ptr.left= node(item)
                    return
                ptr= ptr.left

            else:
                print("Error: Duplicates Found.")

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

    def print_range(self,root,x ,y):
        if root is None:
            return
        
        if y< root.data:
            self.print_range(root.left, x, y)

        elif x> root.data:
            self.print_range(root.right, x, y)

        elif x<=root.data and y>=root.data:
            self.print_range(root.left,x,y)
            print(root.data, end=" ")
            self.print_range(root.right, x ,y)

        else:
            print("ERROR: Invalid range.")
            return
        
t= bst()
t.insert(8)
t.insert(5)
t.insert(17)
t.insert(11)
t.insert(46)

t.display()
print()

print("Range from 0 to 20:",end=" ")
t.print_range(t.start, 0,20)