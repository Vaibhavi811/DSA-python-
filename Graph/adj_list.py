class Graph:
    def __init__(self, isdirected= False):
        self.adj_list={}
        self.isdirected= isdirected

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edges(self,u,v):
        self.add_vertex(u)
        self.add_vertex(v)
        
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)

        if self.isdirected is False and u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def remove_edge(self,u,v):
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

        if self.isdirected is False and v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def display(self):
        print("Adjacency List:")
        for vertex, neighbour in self.adj_list.items():
            print(f"{vertex} --> {neighbour}")

class weighted:
    def __init__(self, isdirected=False):
        self.adj_list= {}
        self.isdirected= isdirected

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]= []

    def add_edges(self,u,v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
         
        self.adj_list[u].append((v,weight))

        if self.isdirected is False:
            self.adj_list[v].append((u,weight))

    def remove_edge(self,u,v,weight):
        if u in self.adj_list:
            self.adj_list[u]= [
                (vertex,weight) for vertex,weight in self.adj_list[u]
                if vertex!=v
            ]

        if self.isdirected is False and v in self.adj_list:
            self.adj_list[v]= [
                (vertex,weight) for vertex,weight in self.adj_list[v]
                if vertex!=u
            ]

    def display(self):
        print("Adjacency List:")
        for key, pair in self.adj_list.items():
            print(f"{key} --> {pair}")


g= Graph(True)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

g.add_edges(1,2)
g.add_edges(1,3)
g.add_edges(2,3)
g.add_edges(3,4)
g.add_edges(2,4)

g.display()

g.remove_edge(2,3)

g.display()

w= weighted()
w.add_vertex(1)
w.add_vertex(2)
w.add_vertex(3)
w.add_vertex(4)

w.add_edges(1,2,4)
w.add_edges(1,3,5)
w.add_edges(2,3,6)
w.add_edges(3,4,7)
w.add_edges(2,4,8)

w.remove_edge(1,3,5)

w.display()