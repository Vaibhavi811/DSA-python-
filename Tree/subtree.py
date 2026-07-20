class node:
    def __init__(self,data):
        self.left= None
        self.data= data
        self.right= None

class Tree:
    def __init__(self):
        self.start= None

    def insert(self,root):
        if root is None:
            value_root=int(input("Enter root value:"))
            if value_root!=-1:
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

            print(value.data, end="  ")
            if value.left:
                queue.append(value.left)
            if value.right:
                queue.append(value.right)

class Solution:
    def isIdentical(self,root,subroot):
        if root is None and subroot is None:
            return True
        if root is None or subroot is None:
            return False
        if root.data== subroot.data:
            return self.isIdentical(root.left,subroot.left) and self.isIdentical(root.right,subroot.right)
        
        return False
    

    def issubtree(self,root,subroot):
        if subroot is None:
            return True
        if root is None:
            return False
        
        if root.data== subroot.data:
            if self.isIdentical(root,subroot):
                return True
            
        return self.issubtree(root.left,subroot) or self.issubtree(root.right,subroot)
    
t= Tree()
t.start= t.insert(t.start)
t.display()

print()

t1= Tree()
t1.start= t1.insert(t1.start)
t1.display()
print()

s= Solution()
ans=s.issubtree(t.start,t1.start)
print("IS t1 a subtree of t?",ans)



