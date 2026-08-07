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

    def topo_sort(self,node, visited, stack, recstack):
        visited.add(node)
        recstack.add(node)

        for neighbours in self.adj_list[node]:
            if neighbours not in visited:
                if self.topo_sort(neighbours, visited, stack, recstack):
                    return True
                
            elif neighbours in recstack:
                return True
            
        recstack.remove(node)
        stack.append(node)
        return False
    
    def topological_sort(self):
        visited= set()
        recstack= set()
        stack= []

        for vertex in self.adj_list:
            if vertex not in visited:
                self.topo_sort(vertex, visited, stack, recstack)

        print("Topological Order:", stack[::-1])

g= graph()

g.add_edges(1,2)
g.add_edges(1,3)
g.add_edges(2,3)
g.add_edges(3,4)
g.add_edges(4,5)
g.add_edges(4,6)
g.add_edges(5,6)

g.display()
print()

g.topological_sort()