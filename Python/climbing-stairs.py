# https://leetcode.com/problems/climbing-stairs


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(n):
           a, b = b, a + b
        return b
