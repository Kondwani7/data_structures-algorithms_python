#normally using elements of one list to creat another list
#e.g prefix sum = x0, x1,x2 in output y0,y1,y2
#output y0=x0, y1=x0+x1, y2=x0+x1+x2
#prefix sum
def prefixSum(arr):
    #initalize with 0s
    ans = [0] * len(arr)
    #firt element is 0
    ans[0] = arr[0]
    #loop from second get sum, similar to fib
    for i in range(1,len(arr)):
        #our answer is the answer at the value before it + ith position of value in array
        ans[i] = ans[i-1] + arr[i]
    return print("prefix sum array:",ans)
arr1 = [3, 2, 5, 43, 2]
arr2 = [1, 2, 3, 4,5,6]
print("inital array:", arr1)
prefixSum(arr1)
print("inital array:", arr2)
prefixSum(arr2)
#prefix product
def prefixProduct(arr):
    def prod(arr):
        ans = 1
        for i in arr:
            ans = ans * i
        return ans
    #get the product starting form the second value arr[1] through our whole array
    ans = [prod(arr[:i+1]) for i in range(len(arr))]
    return print("prefix product", ans)

print("inital array:", arr1)
prefixProduct(arr1)
print("inital array:", arr2)
prefixProduct(arr2)
