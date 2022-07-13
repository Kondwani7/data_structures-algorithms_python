#Depth first Traversal - a stack may be ideal LIFO
#goes from root to deepest path of the graph before backtracking
#keeping track of nodes visited is key
#first recursive
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        #vertices
        self.V = vertices
    #add an edge
    def add_edge(self, u, v):
        self.graph[u].append(v)
    #this will be used by DFS
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)
    #our depth first search
    def DFS(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)
    #breadth first seach - level order traversal
    def BFS(self, s):
        """
        this function traverses a graph with BFS
        Args:
            s - the starting point of traversal
        """
        #mark all vertices not visited
        visited = [False] * (max(self.graph) + 1)
        #use queues FIFO
        queue = []
        queue.append(s)
        visited[s] = True
        #while the queue exists
        while queue:
            #removed element from queue -dequeue
            s = queue.pop()
            print(s, end=" ")
            #for all vertices dequeued s,
            for i in self.graph[s]:
                #if not visited mark it
                if visited[i] == False:
                    queue.append(i)
                    #list as visited now
                    visited[i] = True
    #topological sorting into DAGS -> applications  scheduling jbos: Airflow ETL or AI pipelines
    #topological sorting with DFS fist
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        #visited all node v in graph 
        for i in self.graph[v]:
            #if not vistied
            if visited[i] == False:
                #recusively visit
                self.topologicalSortUtil(i, visited, stack)
        #then append to stack
        stack.append(v)
    #complete topological sort function
    def topologicalSort(self):
        #mark all vertices not visited
        visited = [False] *self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        #print stack
        print(stack[::-1])

print("DFS recursive")
g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 0)
g1.add_edge(2, 3)
g1.add_edge(3,3)
g1.DFS()
print("BFS")
g1.BFS(0)
g2 = Graph(6)
print("topological sort")
g2.add_edge(5, 2)
g2.add_edge(5, 0)
g2.add_edge(4,0)
g2.add_edge(4,1)
g2.add_edge(2,3)
g2.add_edge(3,1)
g1.topologicalSort()
g2.topologicalSort()