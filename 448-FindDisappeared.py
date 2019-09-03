class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        full_list = set(range(1, len(nums) + 1))
        return list(full_list - set(nums))