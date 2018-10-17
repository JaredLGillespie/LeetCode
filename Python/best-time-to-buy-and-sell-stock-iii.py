# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b1, b2, s1, s2 = -float('inf'), -float('inf'), 0, 0
        for price in prices:
            s2 = max(s2, b2 + price)
            b2 = max(b2, s1 - price)
            s1 = max(s1, b1 + price)
            b1 = max(b1, -price)
        return s2
