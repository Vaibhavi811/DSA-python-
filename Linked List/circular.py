class Node():
    def __init__(self,data):
        self.data= data
        self.next= None

class Circular():
    def __init__(self):
        self.head= None

    def insert_first(self,item):
        new_node= Node(item)
        if self.head==None:
            self.head= new_node
            new_node.next= self.head
            
        else:
            ptr=self.head
            while ptr.next!=self.head:
                ptr=ptr.next
            ptr.next=new_node
            new_node.next=self.head
            self.head= new_node

    def insert_last(self,item):
        new_node= Node(item)
        if self.head==None:
            self.head= new_node
            new_node.next= self.head
        else:
            ptr= self.head
            while ptr.next!= self.head:
                ptr= ptr.next
            ptr.next=new_node
            new_node.next= self.head

    def delete_first(self):
        if self.head==None:
            print("Error:List is empty.")
        elif self.head.next==self.head:
            self.head=None
        else:
            ptr= self.head
            while ptr.next!=self.head:
                ptr=ptr.next
            self.head=self.head.next
            ptr.next=self.head

    def delete_last(self):
        if self.head==None:
            print("Error:List is empty.")
        elif self.head.next==self.head:
            self.head=None
        else:
            ptr= self.head
            while ptr.next.next!=self.head:
                ptr= ptr.next
            ptr.next= self.head


    def display(self):
        ptr= self.head
        print("Head",end="-->")
        while True:
            print(ptr.data, end="-->")
            ptr= ptr.next
            if ptr==self.head:
                break

        print("Head")

c= Circular()
c.insert_first(20)
c.insert_first(10)
c.insert_last(30)
c.delete_first()
c.delete_last()
c.display()
    