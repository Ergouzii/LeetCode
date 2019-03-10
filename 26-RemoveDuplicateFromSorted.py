class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        see this link for animation of this problem
        https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247484284&idx=2&sn=c8af62a82a62a21217d0f0b2b5891e4f&chksm=fa0e6cfdcd79e5ebe8726a61f93b834467d29b7d9e60a44feb990388f9e98605ac1e3f7e723d&token=762342620&lang=zh_CN#rd
        """
        if len(nums) <= 1:
            return len(nums)
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right] # all elements before nums[left] are distinct
            right += 1
        return left + 1