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
        """
        this function connects edges to 2 points in a graph
        args:
            - u: source vertex
            - v: destination vertex
        """
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
    #breadth first serach - level order traversal FIFO
    def BFS(self, s):
        """
        this function traverses a graph with BFS
        Args:
            s - the starting point of traversal
        """
        #mark all vertices not visited
        visited = [False] * self.V
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
    #topological sorting into DAGS -> applications  scheduling jobs: Airflow ETL or AI pipelines
    #topological sorting with DFS first
    #topological sort is a series of shortest paths
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        #visit all node v in graph 
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
        #print stack in reverse
        print(stack[::-1])
    #topological sort BFS -> kahn's algorithm topological - weighted graph
    #steps - find number of indegree => incoming edges/ not visted
    #pick vertices with indegree 0 and enqueue add to our initialize queue
    #remove vertex from queue = dequeue
    #increase count of visited nodes-> decrease by in-degree 1 -> in-degree neighbors if 0 enqueue to our queue
    #repeat last step on queue is empty
    #if no of visised nodes != nodes in graph topological sort is not possible
    #Time => O(v + e) numbers vertices + edges
    def topologicalSortBFS(self):
        in_degree = [0] * self.V
        #traverse graph to find indegrees of all vetices
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        #count of visited nodes
        #store of the topological sort
        ans = []
        count = 0
        while queue:
            #store the popped value from list in variable
            u = queue.pop()
            ans.append(u)
            #visit our nodes in the graph based on node u
            for i in self.graph[u]:
                #reduce in_degree - visited by 1
                in_degree[i] -= 1
                #if our neighbors are not visited indgree- 0 , add to our queue
                if in_degree[i] == 0:
                    queue.append(i)
            #increment count to keep track of NO. of visited nodes
            count +=1
        #if count is less than number of nodes in graph
        if count != self.V:
            print("there is a cycle in graph. Topological sort not possible")
        else:
            print(ans)
    #detect a cycle in a graph
    #dfs is the most ideal a stack to keep track of vertices in recursion
    #also keep track of nodes visited and their neighbor
    #function for detech graph
    def isCyClicUtil(self, v, visited, recStack):
        #if the visited and recstack is true
        visited[v] = True
        recStack[v] = True
        #visit v's neighbors and if any stack is visited and in the recstack, the graph is cyclic
        for neighbor in self.graph[v]:
            #univisted neighbors
            if visited[neighbor] == False:
                if self.isCyClicUtil(neighbor, visited, recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                return True

    def isCyCilc(self):
        visited = [False] * (self.V + 1)
        #our recording staack
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyClicUtil(node, visited, recStack) == True:
                    return True
        #if no cycle
        return False
  
        

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
print("topological sort DFS")
g2.add_edge(5, 2)
g2.add_edge(5, 0)
g2.add_edge(4,0)
g2.add_edge(4,1)
g2.add_edge(2,3)
g2.add_edge(3,1)
g1.topologicalSort()
g2.topologicalSort()
print("topological sort BFS")
g1.topologicalSortBFS()
g2.topologicalSortBFS()
#shortest path - unweighed (Bell Ford) and weighed graph/ dijkstra's algorithm
#for shortest path unweight BFS traversal is ideally the best because all the earliest nodes are visited first
#first intialize array not visited
#initialize array dist = [] source vertex .. targret vertex & in essence the path to get to target vertext from source -shortest
#time => O(v+ e)
#forming a edge
def build_graph():
    edges = [
        ['A', 'B'], ['A', 'E'],
        ['A', 'C'], ['B', 'D'],
        ['B', 'E'], ['C', 'F'],
        ['C', 'G'], ['D', 'E']
    ]
    graph = defaultdict(list)

    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

g3 = build_graph()
print("graph 3 built for testing shortest path")
print(g3)
#shortest path
def shortest_pathBFS(graph, start, goal):
    #distance to goal
    dist = []
    #queue to traverse graph from "start" vertex
    queue = [[start]]
    if start == goal:
        print("same node is the shortest path")
        return
    while queue:
        path = queue.pop()
        #last element
        node = path[-1]

        if node not in dist:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                #if we don't find it keep appending neighbor to our new path
                new_path.append(neighbor)
                #eneque the new path to our queue
                queue.append(new_path)
                #if we get to the goal
                if neighbor == goal:
                    print("shortest path: ", *new_path)
                    return
            dist.append(node)
    #if nodes are not connected, we can't find the shortest path
    print("nodes not connected, shortest path not found")
    return


    

shortest_pathBFS(g3, 'C', 'G')
#using adjaceny matrix just for dijkstra
class GraphM:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
    def printAns(self, dist):
        print("vertex \t distance from source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])
    #function to find vertex closest(min distance) from a given set of vertexs
    #will be used in our shortest path tree
    def minDistance(self, dist, sptSet):
        #inital with a high value
        minVal = 1e7
        #search for nearest vertex that's not in the shortest path tree
        for v in range(self.V):
            if dist[v] < minVal and  sptSet[v] == False:
                minVal = dist[v]
                min_index = v
        #keep track of this new nearest vertex not in spt
        return min_index

    def dijkstra(self, src):
        """
        Dijkstra - greedy approach, it always picks the vertex closest to the source
        use a priority queue to store unvisited vertices from our target distance
        it keeps tracks of distances of source to v in a distance table, 
        it does not work with weights = -1
        this table is created after the kth iteration
        in essence it is a sum of shortest path trees
        """
        #inital extremely high distance of all vertices in graph
        dist = [1e7] * self.V
        dist[src] = 0
        #nodes not visited-  shortest path tree
        sptSet = [False] * self.V
        for count in range(self.V):
            #get the minimum distance vertex from all unvisited vertices
            u = self.minDistance(dist, sptSet)
            #place our minimum distance in the shortest path tree 
            sptSet[u] = True
            #update our distance only if the current distance is greater than the new distance
            #and the vertex is not in our shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        return self.printAns(dist) 

g4 = GraphM(9)
g4.graph =  [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

g4.dijkstra(3)
#detecting cycle in graph test
g5 = Graph(4)
g5.add_edge(0,1)
g5.add_edge(0,2)
g5.add_edge(1,2)
g5.add_edge(2, 0)
g5.add_edge(2, 3)
g5.add_edge(3, 3)
print("graph 1")
if g1.isCyCilc() == 1:
    print("Graph has a cycle")
else:
    print("no cycle")
print("graph 5")
if g5.isCyCilc() == 1:
    print("graph is a cylce")
else:
    print("no cycle")
#strongly connected graphs (count)
#all the  vertices are connected by edges are connected in a cycle

class Graph2:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
    #add an edge
    def add_edge(self, u, v):
        self.graph[u].append(v)
    #DFS
    def DFS(self, v, visited_vertex):
        visited_vertex[v] = True
        print(v, end=" ")
        for i in self.graph[v]:
            if not visited_vertex[i]:
                #recurssively updated as visited
                self.DFS(i, visited_vertex)
    #fill order push elements visited using DFS to stack
    def fil_order(self, v, visited_index, stack):
        visited_index[v] = True
        for i in self.graph[v]:
            if not visited_index[i]:
                self.fil_order(i, visited_index, stack)
        stack = stack.append(v)
    #reverse
    def transpose(self):
        g = Graph2(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g
    #now get strongly connected components
    def stronglyConnected(self):
        stack = []
        visited_index = [False] * self.V
        for i in range(self.V):
            if not visited_index[i]:
                self.fil_order(i, visited_index, stack)
        gRev = self.transpose()

        visited_index = [False] * self.V
        #store in ans array
        while stack:
            i = stack.pop()
            #not viisted
            if not visited_index[i]:
                gRev.DFS(i, visited_index)
                print("")
g6 = Graph2(8)
g6.add_edge(0, 1)
g6.add_edge(1, 2)
g6.add_edge(2, 3)
g6.add_edge(2, 4)
g6.add_edge(3, 0)
g6.add_edge(4, 5)
g6.add_edge(5, 6)
g6.add_edge(6, 4)
g6.add_edge(6, 7)
#print storngly connected ccomponents
g6.stronglyConnected()