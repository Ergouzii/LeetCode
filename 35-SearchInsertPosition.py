class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return
        if target > max(nums):
            return len(nums)
        if target not in nums:
            for num in nums:
                if target < num:
                    return nums.index(num)
        return nums.index(target)