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
        it will sift up (swap) values smaller with the ones above it
        until a heap structure is created
        """
        pass

    def siftdown(self, i):
        """
        this function will traverse a heap
        it sift dow (swap) values larger than the ones below it
        until a heap structure is created
        """
        pass
