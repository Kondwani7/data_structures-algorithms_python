#used to literally search an array\
#unordered search - time O(n)
#time O(n) loop through every element worst case
def unorderedSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return print("unordered search: found at position:",i)
    #otherwise just return -1
    return print("unorded search: not found",-1)

arr1 = [3, 22, 1 ,5, 23 ,4, 5, 2, 44, -1, 3, -5, 21, 3, 22 , -5, 2, 2, 78]
unorderedSearch(arr1, -5)
#linear search
def linearSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return print("linear search: found at position:",i)
        
    return print("linear search: not found", -1)
#time O(1)
linearSearch(arr1, 5)
