class graph:
    def __init__(self):
        self.adj_list= {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edges(self, u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)

        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)


    def display(self):
        print("Adjacency List:") 
        for key,pair in self.adj_list.items():
            print(f"{key}-->{pair}") 

    def shortest(self,src,dest):
        distance= {}
        parent={}
        visited= set()
        queue=[]

        distance[src]=0
        parent[src]=None
        visited.add(src)
        queue.append(src)

        while queue:
            curr= queue.pop(0)

            if curr==dest:
                break

            for neighbours in self.adj_list[curr]:
                if neighbours not in visited:
                    distance[neighbours]= distance[curr]+1
                    parent[neighbours]= curr
                    visited.add(neighbours)
                    queue.append(neighbours)

        if dest not in visited:
            print("NO path exist")
            return
        
        path= []
        node= dest

        while node!=None:
            path.append(node)
            node= parent[node]

        path.reverse()

        print("Shortest Path:",path)
        print("Shortest Distance:",distance[dest])

g= graph()

g.add_edges(1,2)
g.add_edges(1,3)
g.add_edges(1,4)
g.add_edges(2,5)
g.add_edges(4,6)
g.add_edges(6,7)
g.add_edges(7,8)
g.add_edges(5,8)
g.add_edges(3,8)

g.shortest(1,8)


