'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

'''
import time
def twoSum(arr,target):
    op = []
    for i in nums:
        for j in nums[nums.index(i)+1::]:
            if target == i + j :
                op.append(nums.index(i))
                op.append(nums.index(j))
    return(op)


nums = [2,7,11,15]
target = 18
print(twoSum(nums,target))