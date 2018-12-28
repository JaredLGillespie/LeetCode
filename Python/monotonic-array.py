# https://leetcode.com/problems/monotonic-array/


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 1: return True
        inc = 0
        prev = A[0]

        for a in A:
            if a < prev:
                if inc == 0: inc = 1
                elif inc == -1: return False
            elif a > prev:
                if inc == 0: inc = -1
                elif inc == 1: return False

            prev = a

        return True
