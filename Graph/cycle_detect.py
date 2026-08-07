# Directed Graph
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
        print("ADjacency List:") 
        for key,pair in self.adj_list:
            print(f"{key}-->{pair}")   

    
    def cycle(self, node, visited, stack):
        visited.add(node)
        stack[node]= True

        for neighbours in self.adj_list[node]:
            if neighbours not in visited:
                if self.cycle(neighbours,visited, stack):
                    return True
            
            elif stack[neighbours]:
                return True
            
        stack[neighbours]= False
        return False
    
g= graph()

g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(2,3)
g.add_edges(3,4)
g.add_edges(3,6)
g.add_edges(6,7)
g.add_edges(7,8)
g.add_edges(8,6)
g.add_edges(4,5)
g.add_edges(5,1)

stack= {}
visited= set()

print("Does the graph contains cycle?", g.cycle(0, visited, stack))