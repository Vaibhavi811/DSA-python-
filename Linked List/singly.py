class Node():
    def __init__(self,data):
        self.data= data
        self.next= None

class Singly():
    def __init__(self):
        self.head= None

    def insert_first(self,item):
        new_node= Node(item)
        new_node.next= self.head
        self.head= new_node

    def insert_last(self,item):
        new_node= Node(item)
        if self.head==None:
            new_node.next= self.head
            self.head= new_node
        else:
            ptr= self.head
            while ptr.next:
                ptr= ptr.next
            ptr.next= new_node

    def delete_first(self):
        if self.head==None:
            print("Error: List is empty.")
        elif self.head.next==None:
            self.head=None
        else:
            self.head=self.head.next

    def delete_last(self):
        if self.head== None:
            print("Error: List is empty.")
        elif self.head.next==None:
            self.head=None
        else:
            ptr= self.head
            while ptr.next.next:
                ptr= ptr.next
            ptr.next=None

    def del_by_value(self,value):
        if self.head.data==value:
            self.head= self.head.next
        else:
            ptr= self.head
            while ptr.next!=None and ptr.next.data!=value:
                ptr= ptr.next
            if ptr.next==None:
                print("Error:Value not found")
            else:
                ptr.next= ptr.next.next

    def display(self):
        ptr= self.head
        print("Head", end="-->")
        while ptr:
            print(ptr.data, end="-->")
            ptr= ptr.next
        print("None")

obj= Singly()
obj.insert_first(27)
obj.insert_last(45)
obj.insert_first(6)
obj.insert_last(5)
obj.insert_last(2)

obj.delete_first()
obj.delete_last()
obj.del_by_value(8)

obj.display()