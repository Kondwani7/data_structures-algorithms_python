#graphs
#graph searching DFS - stack and BFS - queue
#shortest path, djisktra
#topological sort
#graph questions - leetcode
#graph with a matrix
from unicodedata import name


class VertexM:
    def __init__(self, n):
        self.node = n

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
        if u in self.vertices and v in self.vertices:
            #drawing the connection
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

g.print_graph()