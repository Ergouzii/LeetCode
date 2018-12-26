class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if not needle in haystack:
            return -1
        start = 0
        end = len(needle)
        for i in range(len(haystack)):
            if haystack[start:end] == needle:
                return start
            else:
                start += 1
                end += 1