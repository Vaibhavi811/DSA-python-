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

        self.adj_list[v].append((u,weight))

    def remove_edge(self,u,v,weight):
        if u in self.adj_list:
            self.adj_list[u]= [
                (vertex,weight) for vertex,weight in self.adj_list[u]
                if vertex!=v
            ]

        if v in self.adj_list:
            self.adj_list[v]= [
                (vertex,weight) for vertex,weight in self.adj_list[v]
                if vertex!=u
            ]

    def display(self):
        print("Adjacency List:")
        for key, pair in self.adj_list.items():
            print(f"{key} --> {pair}")

    def prim(self,src):
        import heapq
        visited= set()
        queue=[]
        mst=[]

        heapq.heappush(queue,(0,src,None))

        while queue:
            dist,curr,parent= heapq.heappop(queue)

            if len(mst)== len(self.adj_list)-1:
                break

            if curr in visited:
                continue

            visited.add(curr)

            if parent!=None:
                mst.append((parent, curr, dist))

            for neighbours,weight in self.adj_list[curr]:
                if neighbours not in visited:
                    heapq.heappush(queue,(weight,neighbours,curr))

        print("Minimum Spanning Tree:")
        for u,v,weight in mst:
            print(f"{u} -- {v}: ({weight})")

g= graph()

g.add_edges(1,2,5)
g.add_edges(1,3,17)
g.add_edges(2,3,8)

g.prim(1)
