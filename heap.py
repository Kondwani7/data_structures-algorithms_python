#a min heap the top value is the smallest and traversing (sifting) down the heap the values increasing
class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            #loop through the reverse of the array
            for i in range(len(self.heap))[::-1]:
                #shift it down to to get the min heap
                self.siftdown(i)
    
    def siftup(self, i):
        """
        this function will traverse through a heap
        description:
            - it will sift up (swap) values smaller with the ones above it
            - until a heap structure is created
        """
        #or root of tree
        parent = (i -1) //2
        #from parent going down
        while i!= 0 and self.heap[i] < self.heap[parent]:
            #swap values i smaller than parent until a heap is created
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i -1) //2

    def siftdown(self, i):
        """
        this function will traverse a heap
            description:
            - it sift dow (swap) values larger than the ones below it
            - until a heap structure is created
        """
        #left and right of heap
        left = 2*i + 1
        right = 2*i + 2
        #while left or right is smaller than the len of heap and value i is greater than left or right
        while(left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            #check for the smallest nodes between left or right that will be swapped with i
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            #swap smallest with i
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            #until i is the smallest
            i = smallest
            #reset left and right
            left = 2*i + 1
            right = 2*i + 2
    #insert in a heap
    def insert(self, element):
        """
        this function inserts an element in a list
        description:
            - add element to end of list
            - then sift up until we have a heap
        """
        self.heap.append(element)
        #siftup through the list until we have a heap
        self.siftup(len(self.heap) -1)
    #get the min
    #easier because we are just getting the first element
    def get_min(self):
        return self.heap[0] if len(self.help) > 0 else None
    #extract the min
    #we have to not only get it, but remove it from the heap
    def extract_min(self):
        """
        this function will get the minimum and remove it from the list
        Description:
            - find the min(top), swap with the bottom of the heap, pop it
            - then sift down or new first element self.heap[0] to make the array a heap again
        """
        if len(self.heap) == 0:
            return None
        minval = self.heap[0]
        #swap with last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        #pop the old min value
        self.heap.pop()
        #sift down the first element till we have a heap
        self.siftdown(0)
        #return our min
        return minval
    #update by a specif index
    def update_by_index(self, i ,new):
        """
        this function will replace a value with new at index i
        description:
            - if the new value is smaller than old, sift up
            - if he new value is greater than old, sift down
        """
        old = self.heap[i]
        self.heap[i] = new
        if new < old:
            self.siftup(i)
        else:
            self.siftdown(i)
    #update
    def update(self, old ,new):
        """
        this function will update a old value with a new value
        description:
            - get the index of the old value, and replace with the new function
            - use our update_by_index function
        """
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)
    