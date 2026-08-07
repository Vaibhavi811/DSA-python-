class graph:
    def __init__(self):
        self.adj_list= {}
        self.timer=0

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edge(self, u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def remove_edge(self,u,v):
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

        if v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def display(self):
        print("Adjacency List:") 
        for key,pair in self.adj_list.items():
            print(f"{key}-->{pair}")

    def articulation(self, curr, visited, parent, disc, low, art):
        visited.add(curr)
        child=0
        disc[curr]=self.timer
        low[curr]=self.timer
        self.timer+=1

        for neighbours in self.adj_list[curr]:
            if neighbours not in visited:
                parent[neighbours]=curr
                child+=1

                self.articulation(neighbours,visited,parent,disc, low, art)

                low[curr]=min(low[curr],low[neighbours])

                if parent[curr]!=None and low[neighbours]>= disc[curr]:
                    art.append(curr)

            elif neighbours is not parent[curr]:
                low[curr]= min(disc[neighbours],low[curr])

        if parent[curr]==None and child>1:
            art.append(curr)

    def cover(self):
        visited=set()
        disc= {}
        parent={}
        low= {}
        art=[]

        self.timer=0

        for vertex in self.adj_list:
            if vertex not in visited:
                parent[vertex]= None
                self.articulation(vertex,visited, parent, disc, low, art)

        print("Discovery Time:",disc)
        print("LOw Value:",low)

        print("\nArticulation point:")
        for node in sorted(art):
            print(node)

g= graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

g.display()

print()
g.cover()