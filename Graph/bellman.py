class graph:
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

    def bellman(self,src):
        distance={node:float("inf") for node in self.adj_list}
        distance[src]=0

        for i in range(len(self.adj_list)-1):

            for u in self.adj_list:
                for v,weight in self.adj_list[u]:
                    if distance[u]!=float("inf") and distance[v]> distance[u]+weight:
                        distance[v]= distance[u] +weight

    # For checking negative cycle
        for i in range(len(self.adj_list)-1):

            for u in self.adj_list:
                for v, weight in self.adj_list[u]:
                    if distance[u]!=float("inf") and distance[v]> distance[u]+weight:
                        print("No Shortes path. Negative cycle exist.")
                        return

        print(distance)

g= graph(True)

g.add_edges("a","b",11)
g.add_edges("b","c",-5)
g.add_edges("a","c",8)

g.bellman("a")