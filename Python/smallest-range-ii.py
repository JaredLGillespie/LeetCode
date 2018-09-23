# https://leetcode.com/problems/smallest-range-ii


class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        diff = A[-1] - A[0]
        for i in range(len(A) - 1):
            largest = max(A[-1], A[i] + 2 * K)
            smallest = min(A[i + 1], A[0] + 2 * K)
            diff = min(diff, largest - smallest)
        return diff
