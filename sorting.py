#quick sort, spliting an array in  partition then sorting recursively or iteratively
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