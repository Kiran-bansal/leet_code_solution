class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)+1):       
            if nums.count(nums[i]) == 1 :
                return nums[i]
            else:
                continue
        return 0
