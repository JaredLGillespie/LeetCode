# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return sum(int(i) for i in '{0:b}'.format(x ^ y))
