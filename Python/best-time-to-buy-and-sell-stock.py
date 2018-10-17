# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, buy = 0, float('inf')
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit
