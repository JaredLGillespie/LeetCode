# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit, buy = 0, float('inf')
        for price in prices:
            if price < buy:
                buy = price
            else:
                profit += price - buy
                buy = price
        return profit
