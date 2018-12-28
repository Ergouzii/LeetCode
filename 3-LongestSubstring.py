class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        the idea used here is "sliding window"
        window border is [left+1, right]
        window length is (right - left)
        """
        if not s:
            return 0
        dic = {}
        left = -1
        length = 0
        for right, char in enumerate(s):
            left = max(left, dic.get(char, -1))
            dic[char] = right # update the values of keys
            length = max(length, right - left)
        return length
