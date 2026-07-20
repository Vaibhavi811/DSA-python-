class Node:
    def __init__(self,data):
        self.left= None
        self.data= data
        self.right= None

class Binary:
    def __init__(self):
        self.start= None

    def insert_nodes(self,root):
        value= int(input("Enter any value (-1 for None):"))

        if value==-1:
            return None
        
        root= Node(value)
        
        print(f"Enter value to be inserted in left of {value}:")
        root.left= self.insert_nodes(root.left)

        print(f"Enter value to be inserted in right of {value}:")
        root.right= self.insert_nodes(root.right)

        return root
    
    def preorder(self,root):
        if root is None:
            return
        
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def Inorder(self,root):
        if root is None:
            return
        
        self.Inorder(root.left)
        print(root.data, end=" ")
        self.Inorder(root.right)

    def postorder(self,root):
        if root is None:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

b= Binary()
b.start= b.insert_nodes(b.start)

print("Preorder:", end=" ")
b.preorder(b.start)
print()

print("Inorder:",end=" ")
b.Inorder(b.start)
print()

print("Postorder:",end=" ")
b.postorder(b.start)
print()