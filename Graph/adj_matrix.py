class graph:
    def __init__(self, number, isdirected= False):
        self.isdirected= isdirected
        self.number= number
        self.adj_matrix= [[0] * self.number for i in range(self.number)]
        
    def add_edges(self, u,v,weight=1):
        if u<0 or u>=self.number and v<0 or v>=self.number:
            print("ERROR: Invalid vertex")
            return
        
        self.adj_matrix[u][v]= weight

        if self.isdirected is False:
            self.adj_matrix[v][u]= weight

    def remove_edge(self,u,v):
        if u<0 or u>=self.number and v<0 or v>=self.number:
            print("ERROR: Invalid vertex")
            return
        
        self.adj_matrix[u][v]=0

        if self.isdirected is False:
            self.adj_matrix[v][u]=0

    def display(self):
        for vertex in range(self.number):
            print(vertex, end=" | ")
            for j in range(self.number):
                print(self.adj_matrix[vertex][j], end=" ")
            print()


g= graph(5, True)

g.add_edges(0,2)
g.add_edges(1,3)
g.add_edges(1,4)
g.add_edges(2,1)
g.add_edges(3,2)
g.add_edges(3,4)
g.add_edges(4,0)

g.display()

g.remove_edge(4,0)
print()

g.display()