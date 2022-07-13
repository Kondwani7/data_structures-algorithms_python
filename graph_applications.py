#Depth first Traversal - a stack may be ideal LIFO
#goes from root to deepest path of the graph before backtracking
#keeping track of nodes visited is key
#first recursive
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
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

print("DFS recursive")
g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 0)
g1.add_edge(2, 3)
g1.add_edge(3,3)
g1.DFS()
print("BFS")
g1.BFS(0)