# https://leetcode.com/problems/minimum-increment-to-make-array-unique/


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        next_unique = increments = 0

        for a in A:
            increments += max(next_unique - a, 0)
            next_unique = max(next_unique + 1, a + 1)

        return increments
