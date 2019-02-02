# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        out = [0] * len(A)
        l, r = 0, len(A) - 1
        i = len(A) - 1
        while l <= r:
            if abs(A[l]) > abs(A[r]):
                out[i] = A[l]**2
                l += 1
                i -= 1
            else:
                out[i] = A[r]**2
                r -= 1
                i -= 1

        return out
