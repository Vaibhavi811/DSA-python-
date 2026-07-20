class node:
    def __init__(self,data):
        self.left= None
        self.data= data
        self.right= None

class Tree:
    def __init__(self):
        self.start= None

    def level_insertion(self,root):
        if root is None:
            value_root=int(input("Enter root value (-1 for none):"))
            root= node(value_root)

        queue= [root]

        while queue:
            value= queue.pop(0)

            left= int(input(f"Enter value to be inserted in left of {value.data}:"))
            if left!=-1:
                value.left= node(left)
                queue.append(value.left)
            
            right= int(input(f"Enter value to be inserted in right of {value.data}:"))
            if right!=-1:
                value.right=node(right)
                queue.append(value.right)
        
        return root
    
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

    def height(self,root):
        h=0
        if root is None:
            return h
        h=1
        queue=[root]
        while queue:
            value=queue.pop(0)

            if value.left and value.right is None:
                h+=1
                queue.append(value.left)
            elif value.right and value.left is None:
                h+=1
                queue.append(value.right)
            elif value.left and value.right:
                h= h+ max(self.height(value.left),self.height(value.right))
        
        return h
    
    def height2(self,root):
        h=0
        if root is None:
            return h
        
        h= max(self.height2(root.left),self.height2(root.right)) + 1

        return h


t= Tree()
t.start= t.level_insertion(t.start)

t.display()
print()

print("Height of tree:",t.height(t.start))