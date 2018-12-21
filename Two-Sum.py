class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1: # length of nums must be > 1
            return
        dic = dict(zip(nums, range(len(nums)))) # dict with pairings of each num & its index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                result = [dic[diff], dic[nums[i]]]
                result.sort()
                return result
