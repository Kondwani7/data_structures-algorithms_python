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