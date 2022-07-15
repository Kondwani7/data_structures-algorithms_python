#used to literally search an array\
#unordered search - time O(n)

def unorderedSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return print("found at position:",i)
    #otherwise just return -1
    return print("not found",-1)

arr1 = [3, 22, 1 ,5, 23 ,4, 5, 2, 44, -1, 3]
unorderedSearch(arr1, 23)                