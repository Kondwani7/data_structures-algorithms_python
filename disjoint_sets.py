arr1 = [3, 45, 67, 2, 0 , 8, -4 , 23, 7, 12, 13]
arrSet1 = set(arr1)
print(arrSet1)
#relations in a set may be 
# reflextive a ->E S so a in s,
# symmetric a,b ->E S if a R(relationship) b so b R a is also true,
# transitive a,b,c ->E S, if a R b, and b R c, so a R c is also true
# equivalence class: a class an element a ->E S is a subset of S that contains all the elements that are related to a. 
# set operations
# create a equivalence class : set MAKESET(x)
# finding a equivalence class name : find FIND(X) quick find - path compression
# combining equivalence classes : union - UNION(X,Y) quick union size and/or height + path compression

class DisjointSet:
    def __init__(self, n):
        self.MAKESET(n)
    #make set
    def MAKESET(self, n):
        self.S = [-1 for x in range(n)]
    #find
    def FIND(self, X):
        if(self.S[X] < 0):
            return X
        else:
            return self.FIND(self.S[X])
    #union by size
    def UNION(self, root1, root2):
        if self.FIND(root1) == self.FIND(root2) and self.FIND(root1) == -1:
            return None
        if (self.S[root2] < self.S[root1]):
            self.S[root1] == root2
        else:
            self.S[root1] += self.S[root2]
            self.S[root2] = root2
    