class Solution:
    def twoSum(self,nums,target):
        list={}
        for i in range(len(nums)):
            if target-nums[i] in list:
                return[list[target-nums[i]],i]
            list[nums[i]]=i
