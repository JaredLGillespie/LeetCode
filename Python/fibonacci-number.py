# https://leetcode.com/problems/fibonacci-number/


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a, b = 0, 1
        for _ in range(N):
            a, b = b, a + b
        return a
