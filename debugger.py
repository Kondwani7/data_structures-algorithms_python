#lets go
def checkPossiblity( nums):
    count = 0
    for i in range(0, len(nums) -1):
        if nums[i] <= nums[i+1]:
            count+=1
    return count
arr1 =  [4,2,3]
#print(checkPossiblity(arr1))
#print("34" > "43")

