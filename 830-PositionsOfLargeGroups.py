class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        output = []
        start = 0 
        end = 1
        while end < len(S):
            while end < len(S) and S[start] == S[end]:
                print(start,end)
                end += 1
            if (end - start) > 2: # a large group appears
                temp = [start, end - 1]
                output.append(temp)
            start = end # index "start" changes only if a new group appears
        return output
            