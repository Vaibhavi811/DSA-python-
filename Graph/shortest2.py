class graph:
    def __init__(self):
        self.adj_list= {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]= []

    def add_edges(self,u,v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
         
        self.adj_list[u].append((v,weight))

    def remove_edge(self,u,v,weight):
        if u in self.adj_list:
            self.adj_list[u]= [
                (vertex,weight) for vertex,weight in self.adj_list[u]
                if vertex!=v
            ]

    def display(self):
        print("Adjacency List:")
        for key, pair in self.adj_list.items():
            print(f"{key} --> {pair}")

    def kahn(self):
        queue= []
        topo=[]
        indegree={node:0 for node in self.adj_list}

        for vertex in self.adj_list:
            for neighbours,weight in self.adj_list[vertex]:
                indegree[neighbours]+=1

        for vertex in indegree:
            if indegree[vertex]==0:
                queue.append(vertex)

        while queue:
            curr= queue.pop(0)
            topo.append(curr)

            for neighbours,weight in self.adj_list[curr]:
                indegree[neighbours]-=1

                if indegree[neighbours]==0:
                    queue.append(neighbours)

        return topo

    def shortest_path(self,src):
        distance={node: float('inf') for node in self.adj_list}
        parent= {node:None for node in self.adj_list}
        topo= self.kahn()

        distance[src]=0

        for curr in topo:
            if distance[curr]!=float('inf'):
                for neighbours,weight in self.adj_list[curr]:
                    if distance[neighbours] > distance[curr] + weight:
                        distance[neighbours]= distance[curr] +weight
                        parent[neighbours]=curr

        print(f"Shortest distance from {src}:")
        for key,value in distance.items():
            print(f"{key}: {value}")

g= graph()

g.add_edges(1,2,5)
g.add_edges(1,3,-2)
g.add_edges(1,4,1)
g.add_edges(2,5,3)
g.add_edges(3,8,11)
g.add_edges(4,6,4)
g.add_edges(5,8,0)
g.add_edges(6,7,7)
g.add_edges(7,8,-1)

g.shortest_path(1)

                
