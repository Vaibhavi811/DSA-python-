class Node():
    def __init__(self,data):
        self.pre= None
        self.data= data
        self.next= None

class Doubly():
    def __init__(self):
        self.head= None

    def insert_first(self,item):
        new_node= Node(item)
        if self.head!=None:
            self.head.pre= new_node

        new_node.next= self.head
        self.head= new_node

    def insert_last(self,item):
        new_node= Node(item)
        if self.head==None:
            new_node.next=self.head
            self.head= new_node
        else:
            ptr= self.head
            while ptr.next:
                ptr= ptr.next
            ptr.next= new_node
            new_node.pre= ptr

    def delete_first(self):
        if self.head==None:
            print("Error:List is empty.")
        elif self.head.next==None:
            self.head=None
        else:
            self.head= self.head.next
            self.head.pre= None

    def delete_last(self):
        if self.head==None:
            print("Error:List is empty.")
        elif self.head.next==None:
            self.head=None
        else:
            ptr= self.head
            while ptr.next.next:
                ptr= ptr.next
            ptr.next= None

    def del_by_value(self,value):
        if self.head==None:
            print("Error:List is empty.")
        elif self.head.data== value:
            self.head=self.head.next
            self.head.pre= None
        else:
            ptr= self.head
            while ptr.next!=None and ptr.next.data!=value:
                ptr= ptr.next
            if ptr.next==None:
                print("Error:Value not found")
                return
            ptr.next= ptr.next.next
            
            
    def display(self):
        ptr= self.head
        print("Head",end="<-->")
        while ptr:
            print(ptr.data, end="<-->")
            ptr= ptr.next
        print("None")

    def rev_display(self):
        ptr= self.head
        while ptr.next:
            ptr= ptr.next
        print("None",end="<-->")
        while ptr:
            print(ptr.data, end="<-->")
            ptr= ptr.pre
        print("Head")


d= Doubly()
d.insert_first(20)
d.insert_first(10)
d.insert_last(30)
d.insert_last(40)

d.display()
d.rev_display()

d.delete_first()
d.delete_last()
d.del_by_value(30)

d.display()