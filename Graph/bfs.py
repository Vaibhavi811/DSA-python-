class graph:
    def __init__(self, isdirected= False):
        self.adj_list= {}
        self.isdirected= isdirected

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]= []

    def add_edges(self, u,v):
        self.add_vertex(u)
        self.add_vertex(v)

        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)

        if self.isdirected is False and u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def display(self):
        print("Adjacency List:")
        for key,pair in self.adj_list.items():
            print(f"{key} --> {pair}")

    def bfs(self,node):
        queue=[node]
        visited= set()

        while queue:
            current= queue.pop(0)

            if current not in visited:
                print(current,end=" ")
                visited.add(current)

            for elements in self.adj_list[current]:
                if elements not in visited:
                    queue.append(elements)


g= graph()

g.add_edges(0,1)
g.add_edges(0,2)
g.add_edges(1,3)
g.add_edges(2,4)
g.add_edges(3,4)
g.add_edges(3,5)
g.add_edges(4,5)
g.add_edges(5,6)

g.display()

g.bfs(0)

'''

  1 - 3 \
 /    |  \
0     |   5 - 6
 \    |  /
  2 - 4 /

'''