class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp1 = 1
        dp2 = 2
        dp_step = 0
        if n <= 1:
            return dp1
        if n == 2:
            return dp2
        while n > 2:
            dp_step = dp1 + dp2
            dp1 = dp2
            dp2 = dp_step
            n -= 1
        return dp_step
        