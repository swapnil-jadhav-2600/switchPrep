'''
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

nums = [1,1,1,3,3,4,3,2,4,2]
#=====================================================================================================================================
# PYTHON WAY

print(False if len(set(nums)) == len(nums) else True) 

#=====================================================================================================================================
# ACTUAL WAY

def dupCheck(nums):
    temp = nums[0]
    for i in range(1,len(nums)):
        if temp == nums[i]:
            return True
    return False

print(dupCheck(nums))
