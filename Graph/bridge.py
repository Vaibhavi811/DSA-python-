class graph:
    def __init__(self):
        self.adj_list= {}
        self.timer=0

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edge(self, u,v):
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
        print("Adjacency List:") 
        for key,pair in self.adj_list.items():
            print(f"{key}-->{pair}") 

    def bridge(self,curr,visited,parent,discovery_time,low,bridge):
        visited.add(curr)

        discovery_time[curr]=self.timer
        low[curr]=self.timer
        self.timer+=1

        for neighbours in self.adj_list[curr]:
            if neighbours== parent[curr]:
                continue

            if neighbours not in visited:
                parent[neighbours]= curr

                self.bridge(neighbours,visited, parent,discovery_time,low,bridge)

                low[curr]= min(low[curr],low[neighbours])

                if low[neighbours]> discovery_time[curr]:
                    bridge.append((curr,neighbours))

            else:
                low[curr]= min(discovery_time[neighbours],low[curr])

    def cover(self):
        visited= set()
        discovery_time= {}
        low={}
        parent={}
        bridge=[]

        self.timer=0

        for vertex in self.adj_list:
            if vertex not in visited:
                parent[vertex]= None
                self.bridge(vertex,visited,parent,discovery_time,low,bridge)

        print("Discovery Time:",discovery_time)
        print("Low value:",low)

        print("\nBridge:")
        for u,v in bridge:
            print(f"{u}--{v}")

g= graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

g.display()

print()
g.cover()
