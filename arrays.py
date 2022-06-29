import array as arr
from typing import List

a = arr.array('i',[1,2,3])
for i in range(0, 3):
    print(a[i], end=' ')
print()
b = arr.array('d', [3.4, 2.4, 5.44, 0.56])
for i in range(0, 4):
    print(b[i], end=" ")
print()

#get a specific element in a array
print(f"third element in array: {a[2]}")
#append at the end
a.append(4)
#append at a specific position
# first position  (0)
a.insert(0,0)
#third position (2)
a.insert(2,2)
for i in range(0, 6):
    print(a[i], end=' ')
print()
#remove an element at a specific position (4)
a.pop(4)
for i in range(0,5):
    print(a[i], end=' ')
print()
#add 3 back
a.insert(4,3)
#print(a)
#slicing an array, elements in the 4 position and below
sliced_arr1 = a[:4]
#elements after the 4th postion
sliced_arr2 = a[4:]
for i in range(0,4):
    print(sliced_arr1[i], end=" ")
print("first 4 elements")
#last 2
for i in range(0,2):
    print(sliced_arr2[i], end=" ")
print("last 2 elements")
#reverse an array
reversed_arr = a[::-1]
for i in range(0 ,6):
    print(reversed_arr[i], end=" ")
print("reversed array")
#search array
print(f"third element in array: {a.index(3)}")
print(f"length of array: {len(a)}")
#remove even elements in a array
def remove_even(x):
    for i in x[:]:
        if (i%2) == 0:
            x.remove(i)
    return x

arr3 = [3, 5, 7, 8, 3, 12, 3]
arr3
print(remove_even(arr3))
#remove odd
def remove_odd(x):
    for i in x[:]:
        if (i%2) != 0:
            x.remove(i)
    return x

arr4 = [3, 22, 4 ,55, 17, 559, 2 ,8]
print(remove_odd(arr4))
#min max as a pair
class pair:
    def __init__(self):
        self.min = 0
        self.max = 0
#get the minimum and maximum
def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()
    #if only 1 element
    if n ==1:
        minmax.max = arr[0]
        minmax.min = arr[0]
    #if more than one element
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]
    #more than 2 elements
    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax

arr5 = [39, 2 , 44, 22, -4, -22, 45, 22, 12 ,64, 88, 44, 44,  9, 17, 33]
#sort array
#arr5.sort()
#print(arr5)
arr5_length = len(arr5)

minmax_arr5 = getMinMax(arr5, arr5_length)
print(f"The minimum element in the array is: {minmax_arr5.min}")
print(f"The maximum element in the array is: {minmax_arr5.max}")

#find the second largest element in the array
def getSecondMax(arr, arr_size):
    #if only one element in the array
    if (arr_size < 2):
        return arr
    #first sort the array
    arr.sort()
    #get from second last in the list
    for i in range(arr_size - 2, -1, -1):
        #if not the second largest element
        if arr[i] != arr[arr_size - 1]:
            print(f"second largest element: {arr[i]}")
        return

getSecondMax(arr5, arr5_length)
print([4,5])
#leet code
#remove duplicates in a list
class solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
        return k
#remove an elemnt
class solution2:
    def  removeElement(self, nums: List[int], val:int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
        return k
#two sum
class solution3:
    def twoSum(self, nums, target):
        #hash map
        prevMap = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in prevMap:
                return [prevMap[diff], i]
            #if the target is not in the hashmap
            prevMap[j] = i
        return