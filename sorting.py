#quick sort, spliting an array in  partiion then sorting recursively or iteratively
def partition( l, r, nums ):
    
    #randome numbe pointer is our l
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