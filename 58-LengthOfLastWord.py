class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        s = s.strip()
        for i in reversed(range(len(s))):
            if s[i] == ' ':
                break
            length += 1
        return length
        