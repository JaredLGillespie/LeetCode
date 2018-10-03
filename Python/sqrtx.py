# https://leetcode.com/problems/sqrtx


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x

        while l <= r:
            m = (l + r) // 2
            s = m * m

            if s <= x:
                l = m + 1
            else:
                r = m - 1
        return l - 1
