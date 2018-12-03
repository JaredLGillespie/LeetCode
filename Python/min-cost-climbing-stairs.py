# https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    def minCostClimbingStairs(self, cost):
        a, b = 0, 0
        for c in cost: a, b = b, min(a + c, b + c)
        return min(a, b)
