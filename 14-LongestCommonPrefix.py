class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_len = min(len(s) for s in strs)
        if min_len == 0:
            return ''
        prefix_len = -1
        for i in range(min_len):
            current_char = strs[0][i]
            if all(s[i] == current_char for s in strs):
                prefix_len = i
            else:
                break
        return '' if prefix_len == -1 else strs[0][: prefix_len+1]