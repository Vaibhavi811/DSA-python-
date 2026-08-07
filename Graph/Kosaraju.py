class graph:
    def __init__(self):
        self.adj_list= {}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]

    def add_edge(self, u,v):
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

    def kosaraju(self, curr, visited, stack):
        visited.add(curr)

        for neighbours in self.adj_list[curr]:
            if neighbours not in visited:
                self.kosaraju(neighbours, visited, stack)

        stack.append(curr)

    def dfs_reverse(self,curr,visited, reverse):
        visited.add(curr)
        print(curr, end=" ")

        for neighbours in reverse[curr]:
            if neighbours not in visited:
                self.dfs_reverse(neighbours, visited, reverse)

    def cover(self):
        visited= set()
        stack= []

        for vertex in self.adj_list:
            if vertex not in visited:
                self.kosaraju(vertex,visited,stack)

        reverse={}
        for node in self.adj_list:
            reverse[node]= []

        for u in self.adj_list:
            for v in self.adj_list[u]:
                reverse[v].append(u)

        print("/nReversed Graph:")
        for key,value in reverse.items():
            print(f"{key}--{value}")

        visited=set()

        while stack:
            node= stack.pop()

            if node not in visited:
                self.dfs_reverse(node, visited, reverse)
                print()

g=graph()

g.add_edge('A','B')
g.add_edge('B','C')
g.add_edge('C','D')
g.add_edge('D','A')
g.add_edge('D','E')
g.add_edge('E','F')
g.add_edge('F','G')
g.add_edge('G','E')

g.cover()

