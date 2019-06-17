class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return
        i = 0
        temp = nums[i]
        while i < len(nums) - 1:
            i += 1 
            temp = temp ^ nums[i]
        return temp
