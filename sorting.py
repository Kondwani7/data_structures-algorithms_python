#quick sort, spliting an array in  partition then sorting recursively or iteratively
import math


def partition( l, r, nums ):
    
    #random number pointer is our l
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            #swap values smaller than pivot to front
            nums[i] , nums[ptr] = nums[ptr], nums[i]
            #move to next point
            ptr+=1
    #finally swap last element with the indexed number
    nums[ptr], nums[i] = nums[i], nums[ptr]
    return ptr
#quick sort
def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        #move down from right to front of list
        quicksort(l, pi - 1, nums)
        #move up recursively from left to end of list
        quicksort(pi+ 1, l, nums)
    return nums

arr1 = [3, 45, 67, 2, 0 , 8, -4 , 23, 7, 12, 13]
print("initial array:", arr1)
print("quicksort:", quicksort(0, len(arr1) -1, arr1))
#merge sort split at mid point not a roandom pivot
def MergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        #before mid point
        left = arr[:mid]
        #after midpoint
        right = arr[mid:]
        #recurisvely sort on left and right
        MergeSort(left)
        MergeSort(right)
        i=j=k=0
        #two points i and j loop through list from right and left
        while i<len(left) and j<len(right):
            #if i at left is smaller than right, update array at index k with left
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            #else if j is smaller in right, update array at index k with right 
            else:
                arr[k] = right[i]
                j+=1
            #if equal just increment k index
            k+=1
        #then update arr with left at index k while going through left
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        #and update arr with right at index k while going through rigt
        while j<len(right):
            arr[k] =right[j]
            j+=1
            k+=1
MergeSort(arr1)
print("merge sort array", arr1)
#linear sorting
#counting sort
#its sorts an array by counting the number of occcurences of an elem in a array
#sorted in a auxillary(temp) array then sorted by 
# mapping count as the index of the auxillary(temp) array
#e.g find the max element in a given array
def countingSort(arr):
    #time O(n+k) k eleemnt in list
    """
    target array e.g [2, 0 ,1, 4, 5, 2, 1] get , max, assort in descending order
    sort the count of our target array in a temp array e.g 
    store cumlative sum of elements in a array e.g [2, 2, 3, 7, 12, 14, 15]
    get the index of every element in the original array and 
    restore it and decrease count stored by 1
    """
    size = len(arr)
    ans = [0] * size
    #initialize ccount
    count = [0] * 10
    #store elements in count array
    for i in range(0, size):
        count[arr[i]] +=1
    #store cumlative count
    for i in range(1, 10):
        count[i] += count[i-1]
    #find index of elems in original array in the count array
    #place elements in count array
    i = size -1
    while i>=0:
        ans[count[arr[i]] - 1] = arr[i]
        #reduce count
        count[arr[i]] -=1
        #reduce i
        i -= 1
    #copy sorted elements into original arry
    for i in range(0, size):
        arr[i] = ans[i] 
arr3 = [4, 2, 2, 8, 3, 3, 1]
print("inital array:", arr3)
countingSort(arr3)
print("counting sort array:",arr3)
#bucket sort
#works well when the input is drawn from a fixed set k integers
#uses hashing to partition certain keys of an array
#
def bucketSort(arr):
    """
    create an empty arr of buckets n based on array size
    for every elem in arr, insert in bucket array bucket[n * arr[i]]
    sort buckets with insertion sort
    concatenate all sorted buckets and return
    """
    #sorts array values in buckets ,e.g 1-5 , 5-10 etc buckets
    bucket = []
    #initialize with empty buckets
    for i in range(len(arr)):
        bucket.append([])
    #insert into perspective buckets
    for n in arr:
        index_buc = int(10 *n)
        bucket[index_buc].append(n)
    #sort eleemnts in bucket
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])
    #get our sorted elements
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k +=1
    return arr
#bucket time O(n + k), worse case(n^2)
arr2 =  [.42, .32, .33, .52, .37, .47, .51]
print("bucket sort", bucketSort(arr2))
#radix sort
#it groups elements in some place value 
# then sorting in increasing or decreasing order 