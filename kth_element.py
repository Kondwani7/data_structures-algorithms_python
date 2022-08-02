#this will deal with algorithms handling the kth smallest & largest element in a array matrix, etc
#Q1 - find kth smallest element in a unsorted array
#e.g arr1 = [7, 10, 4, 3, 20, 15], k= 3 , output = 7
#option 1 is just to sort the algorithm
def kthSmallest(arr, k):
    arr.sort()
    return arr[k- 1]

arr1 = [7, 10, 4, 3, 20, 15]
print(kthSmallest(arr1, 3))