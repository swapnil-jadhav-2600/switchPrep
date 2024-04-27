'''
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30

'''



nums = [1,2,3,4]
lis = []
temp = nums[0]

for i in range(len(nums)):
    nums = [1,2,3,4]
    prod = 1
    lis = nums
    lis.remove(nums[i])
    for j in range(len(lis)):
        prod = prod*lis[j]

    print(prod)


