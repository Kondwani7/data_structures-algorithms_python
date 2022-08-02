#this will deal with algorithms handling the kth smallest & largest element in a array matrix, etc
#Q1 - find kth smallest element in a unsorted array
#e.g arr1 = [7, 10, 4, 3, 20, 15], k= 3 , output = 7
#option 1 is just to sort the algorithm
#time O(nlogn)
def kthSmallest(arr, k):
    arr.sort()
    return arr[k- 1]

arr1 = [7, 10, 4, 3, 20, 15]
print(kthSmallest(arr1, 3))
#sets because they demonstrate the distinct items in array
def kthSmallest2(arr, k):
    n = len(arr)
    s = set(arr)
    for i in s:
        if k == 1:
            print(i)
            break
        k -= 1

print(kthSmallest2(arr1, 3))
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

print(kthSmallestMinHeap(arr1, 3))