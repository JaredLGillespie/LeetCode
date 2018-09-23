# https://leetcode.com/problems/smallest-range-i


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        smallest = min(A)
        largest = max(A)

        if largest - smallest < K * 2:
            return 0

        return largest - smallest - K * 2
