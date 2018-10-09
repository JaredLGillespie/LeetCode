# https://leetcode.com/problems/divide-two-integers


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0

        while dividend >= divisor:
            t, c = divisor, 1
            while t <= dividend:
                t <<= 1
                c <<= 1
            res += c >> 1
            dividend -= t >> 1

        if neg:
            return -res

        return min(2**31 - 1, res)
