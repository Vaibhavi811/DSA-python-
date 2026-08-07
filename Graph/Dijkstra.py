class graph:
    def __init__(self, isdirected=False):
        self.adj_list= {}
        self.isdirected= isdirected

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]= []

    def add_edge(self,u,v, weight):
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

    def dijkstra(self,src):
        import heapq
        distance= {node:float('inf') for node in self.adj_list}
        parent= {node:None for node in self.adj_list}
        queue=[]

        distance[src]=0
        heapq.heappush(queue,(0,src))

        while queue:
            dist,curr= heapq.heappop(queue)

            if dist > distance[curr]:
                continue

            for neighbours,weight in self.adj_list[curr]:
                if distance[neighbours]> distance[curr] + weight:
                    distance[neighbours]= distance[curr]+ weight
                    parent[neighbours]=curr

                    heapq.heappush(queue,(distance[neighbours],neighbours))

        print(f"Shortest path from {src}")
        for key,val in distance.items():
            print(f"{key}:{val}")

g= graph()

g.add_edge(0,1,5)
g.add_edge(1,3,2)
g.add_edge(3,2,6)
g.add_edge(2,0,8)
g.add_edge(1,2,9)

g.dijkstra(0)

