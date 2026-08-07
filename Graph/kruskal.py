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

    def find_parent(self, node, parent):
        if node!=parent[node]:
            return self.find_parent(parent[node], parent)

        return parent[node]

    def union(self,parent, rank, u,v):
        root_u= self.find_parent(u,parent)
        root_v= self.find_parent(v,parent)

        if root_u==root_v:
            return False
        else:
            if rank[root_u]>rank[root_v]:
                parent[root_v]=root_u
            elif rank[root_v]>rank[root_u]:
                parent[root_u]=root_v
            else:
                parent[root_v]=root_u
                rank[root_u]+=1

        return True

    def kruskal(self):
        visited= set()
        edges= []

        for u in self.adj_list:
            for v,weight in self.adj_list[u]:
                if (v,u) not in visited:
                    visited.add((u,v))
                    edges.append((weight,u,v))

        edges.sort()

        parent={}
        rank={}

        mst=[]
        totalcost=0

        for node in self.adj_list:
            parent[node]=node
            rank[node]=0

        for weight,u,v in edges:
            if self.union(parent,rank,u,v):
                mst.append((u,v,weight))
                totalcost+=weight

            if len(mst)== len(self.adj_list)-1:
                break

        print("Minimum Spanning Tree:")
        for u,v,weight in mst:
            print(f"{u}--{v}:({weight})")

        print("Total Cost:",totalcost)

g=graph()

g.add_edges("A","B",2)
g.add_edges("A","C",15)
g.add_edges("B","C",3)
g.add_edges("B","D",8)
g.add_edges("C","D",4)

g.kruskal()