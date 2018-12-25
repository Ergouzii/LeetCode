class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        len_lis = []
        for s in strs:
            len_lis.append(len(s))
        min_len = min(len_lis)
        if min_len == 0:
            return ''
        temp = []
        for i in range(min_len):
            for s in strs:
                temp.append(s[i])
            print(temp)
            if len(set(temp)) != (i + 1): # if not all same
                temp = temp[:-len(strs)] # pop the different prefixes
                temp = temp[::len(strs)] # remove duplicate chars
                return ''.join(temp)
        print(temp)
        temp = temp[::len(strs)] # remove duplicate chars
        return ''.join(temp)