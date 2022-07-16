#graphs
#graph searching DFS - stack and BFS - queue
#shortest path, djisktra
#topological sort
#graph questions - leetcode
#graph with a matrix


class VertexM:
    def __init__(self, n):
        self.node = n
#O(n^2)
class GraphM:
    vertices = {}
    edges = []
    edges_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, VertexM) and vertex.node not in self.vertices:
            self.vertices[vertex.node] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edges_indices[vertex.node] = len(self.edges_indices)
            return True
        else:
            return False
    def add_edge(self, u, v, weight=1):
        #matching row to column
        if u in self.vertices and v in self.vertices:
            #drawing the connection an attaching the weight
            self.edges[self.edges_indices[u]][self.edges_indices[v]] = weight
            self.edges[self.edges_indices[v]][self.edges_indices[u]] = weight
            return True
        else: 
            return False

    def print_graph(self):
        #sorted in ascending order
        for v, i in sorted(self.edges_indices.items()):
            print(v + '', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')

g = GraphM()
a = VertexM('A')
g.add_vertex(a)
g.add_vertex(VertexM('B'))
#adding vertexes
for i in range(ord('A'), ord('K')):
    g.add_vertex(chr(i))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
print("graph adjaceny matrix")
g.print_graph()

#graph adjaceny list
class Vertex:
    def __init__(self, node):
        self.node = node
        self.neighbors = list()
    
    def add_neighbor(self, v, weight):
        if v not in self.neighbors:
            self.neighbors.append((v, weight))
            self.neighbors.sort()
#list graph - o(logn)
class Graph:
    vertices = {}
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.node not in self.vertices:
            self.vertices[vertex.node] = vertex
            return True
        else:
            return False
    def add_edge(self, u, v, weight=0):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v, weight)
            self.vertices[v].add_neighbor(u, weight)
            return True
        else:
            return False
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
    
g2 = Graph()
a = Vertex('A')
g2.add_vertex(a)
g2.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g2.add_vertex(Vertex(chr(i)))

for edge in edges:
    g2.add_edge(edge[:1], edge[1:])
print("graph adjaceny list")
g2.print_graph()
