class Solution():
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        note: the max num in nums is len(nums)
        """
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums)
        