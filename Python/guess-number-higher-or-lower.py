# https://leetcode.com/problems/guess-number-higher-or-lowe


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            g = guess(m)
            if g == 0:
                return m
            if g == -1:
                r = m - 1
            else:
                l = m + 1
        return l
