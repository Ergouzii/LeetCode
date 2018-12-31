class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        max_profit = 0
        for p in prices:
            buy = min(buy, p)
            max_profit = max(max_profit, p - buy)
        return max_profit
            