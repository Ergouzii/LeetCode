class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        
        new_x = 0
        while x != 0:
            pop = x % 10
            x = x // 10
            new_x = new_x * 10 + pop

        new_x = new_x * sign

        if new_x >= 2**31 or new_x < -2**31:
            return 0

        return new_x