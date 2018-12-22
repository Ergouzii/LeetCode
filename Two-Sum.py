class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1: # length of nums must be > 1
            return
        dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                result = [i, dic[diff]]
                result.sort()
                return result
            dic[nums[i]] = i