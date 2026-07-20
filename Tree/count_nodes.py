class node:
    def __init__(self,data):
        self.left=None
        self.data= data
        self.right= None

class Tree:
    def __init__(self):
        self.start= None

    def level_insertion(self,root):
        if root is None:
            value_root= int(input("Enter root value:"))
            root= node(value_root)

        queue=[root]
        while queue:
            value= queue.pop(0)
            
            left=int(input(f"Enter value to be inserted in left of {value.data}:"))
            if left!=-1:
                value.left= node(left)
                queue.append(value.left)

            right=int(input(f"Enter value to be inserted in right of {value.data}:"))
            if right!=-1:
                value.right= node(right)
                queue.append(value.right)

        return root
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

    def Count_nodes(self):
        count=0
        if self.start is None:
            return count
        
        count=1
        queue=[self.start]

        while queue:
            value= queue.pop(0)

            if value.left:
                count+=1
                queue.append(value.left)

            if value.right:
                count+=1
                queue.append(value.right)
                
        return count

t= Tree()
t.start= t.level_insertion(t.start)
t.display()
print()

print("Total number of nodes:", t.Count_nodes())