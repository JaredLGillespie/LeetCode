# https://leetcode.com/problems/zigzag-conversion


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        neg = 1
        if x[0] == '-':
            neg = -1
            x = x[1:]
        x = ''.join(reversed(x))
        x = int(x) * neg
        if not (-2**31 <= x <= 2 ** 31 - 1):
            return 0
        return x
