# https://leetcode.com/problems/binary-gap/


class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        biggest_gap = 0
        j = -1
        for i in range(N):
            if N & (1 << i):
                if j != -1: biggest_gap = max(biggest_gap, i - j)
                j = i
        return biggest_gap
