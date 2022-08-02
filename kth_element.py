#this will deal with algorithms handling the kth smallest & largest element in a array matrix, etc
#Q1 - find kth smallest element in a unsorted array
#e.g arr1 = [7, 10, 4, 3, 20, 15], k= 3 , output = 7
#option 1 is just to sort the algorithm
#time O(nlogn)
import sys


def kthSmallest(arr, k):
    arr.sort()
    return arr[k- 1]

arr1 = [7, 10, 4, 3, 20, 15]
print("kth smallest element by sorting in ascending order", kthSmallest(arr1, 3))
#sets because they demonstrate the distinct items in array
def kthSmallest2(arr, k):
    n = len(arr)
    s = set(arr)
    for i in s:
        if k == 1:
            print(i)
            break
        k -= 1
print("kth smallest element with a set", kthSmallest2(arr1, 3))
#using a min heap
#time O(nlogn)
class MinHeap:
    def __init__(self, a, size):
        #list of elements in a array
        self.harr = a
        #max capacity of min heap
        self.capacity = None
        #curent number of elements in the heap
        self.heap_size = size
        i = int((self.heap_size - 1) /2)
        while i >= 0:
            self.minHeapify(i)
            i -= 1
    #parent of heap
    def parent(self, i):
        return (i -1 ) /2
    #left of min heap
    def left(self, i):
        return 2* i + 1
    #right of min heap
    def right(self, i):
        return 2 * i + 2
    #get minimum
    def getMin(self):
        return self.harr[0]
    #remove minimum element from heap
    def extract_min(self):
        if self.heap_size == 0:
            return float("inf")
        root = self.harr[0]
        if self.heap_size > 1:
            #swapfirst  with last eelement
            self.harr[0] = self.harr[self.heap_size -1]
            #then shift down to heapify
            self.minHeapify(0)
        #reduce heap size and get our root
        self.heap_size -= 1
        return root
    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if ((l < self.heap_size) and (self.harr[l] < self.harr[i])):
            smallest = l
        if ((r < self.heap_size) and (self.harr[r] < self.harr[smallest])):
            smallest = r
        if smallest != i:
            #swap
            self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
            self.minHeapify(smallest)

#kth smallest wit h min heap
def kthSmallestMinHeap(arr, k):
    mh = MinHeap(arr, len(arr))
    for i in range(k -1):
        mh.extract_min()
    return mh.getMin()

print("kth smallest element with a minheap: ",kthSmallestMinHeap(arr1, 3))
#quick sort - we use a pivot and sort until we get to the kth element
def kthSmallestQuickSort(arr,l, r, k):
    if (k > 0 and k <= r -l + 1):
        pos = partition(arr, l, r)
        #position is the same as k
        if (pos - 1 == k - 1):
            return arr[pos]
        #position is greater move down array, reduce right by pos
        if (pos - 1 > k - 1):
            return kthSmallestQuickSort(arr, l, pos - 1, k)
        #else move up array
        if (pos - 1 < k -1):
            return kthSmallestQuickSort(arr, pos + 1, r, k - pos + l - 1 )
    return sys.maxsize

def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            #swap to all smaller elements on the left
            arr[i], arr[j] = arr[j], arr[i]
            i+= 1
    #then swap last element
    arr[i], arr[r] = arr[r], arr[i]
    return i

print("kth largest element with quicksort", kthSmallestQuickSort(arr1, 0, len(arr1) - 1, 3))
#find kth smallest with binary search
def count(nums, mid):
    cnt = 0
    for i in range(len(nums)):
        if nums[i] <= mid:
            cnt += 1
    return cnt

def kthSmallestBS(arr, k):
    low = sys.maxsize
    high = -sys.maxsize - 1
    for i in range(len(arr)):
        low = min(low, arr[i])
        high = max(high, arr[i])
    while low < high:
        mid = (low + high) // 2
        if count(arr, mid) < k:
            low = mid + 1
        else:
            high = mid
    return low

print("k smallest element with binary search:", kthSmallestBS(arr1, 3))

#k largest element from 2  sorted arrays

#find 2 smallest numbers in a array
#brute force would just be to sort in decreasing order
#and get the 0, 1 index elements in our array
def firstSecondSmallestElems(arr):
    arr.sort()
    return (arr[0], arr[1])
arr2 = [3, 22, 1, 2, 3, 44, 0, -4, 1]
print("brute force smallest and second smallest items in array: ", firstSecondSmallestElems(arr2))