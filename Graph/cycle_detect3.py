class graph:
    def __init__(self):
        self.adj_list= {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edges(self, u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj_list[u].append(v)
        
    def remove_edge(self,u,v):
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

    def display(self):
        print("Adjacency List:") 
        for key,pair in self.adj_list.items():
            print(f"{key}-->{pair}")

    def cycle(self):
        queue= []
        topo=[]

        indegree= {node:0 for node in self.adj_list}

        for vertex in self.adj_list:
            for neighbours in self.adj_list[vertex]:
                indegree[neighbours]+=1

        for vertex in indegree:
            if indegree[vertex]==0:
                queue.append(vertex)

        if len(queue)==0:
            return True
        
        while queue:
            curr= queue.pop(0)
            topo.append(curr)

            for neighbours in self.adj_list[curr]:
                indegree[neighbours]-=1

                if indegree[neighbours]==0:
                    queue.append(neighbours)

        return len(topo)!= len(self.adj_list)
    
g= graph()

g.add_edges(1,2)
g.add_edges(2,3)
g.add_edges(3,4)
g.add_edges(4,5)
g.add_edges(5,6)
g.add_edges(6,4)

print("Does graph contain cycle?",g.cycle())