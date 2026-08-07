# Undirected Graph
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
        self.adj_list[v].append(u)
        
    def remove_edge(self,u,v):
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

        if v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

    def display(self):
        print("ADjacency List:") 
        for key,pair in self.adj_list:
            print(f"{key}-->{pair}") 

    def cycle(self, node, visited):
        queue= [(node,-1)]
        visited.add(node)

        while queue:
            curr,parent= queue.pop(0)

            for neighbour in self.adj_list[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour,curr))

                elif parent!=neighbour:
                    return True
                

        return False
    

g= graph()

g.add_edges(1,2)
g.add_edges(2,3)
g.add_edges(3,4)
g.add_edges(3,5)
g.add_edges(2,6)
g.add_edges(6,5)

g.remove_edge(6,5)

visited= set()
print("Does graph contains cycle?",g.cycle(3,visited))