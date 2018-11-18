# https://leetcode.com/problems/valid-mountain-array/

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2: return False
        if A[0] > A[1]: return False

        increasing = True
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                if not increasing: return False
            elif A[i] < A[i - 1]:
                increasing = False
            else:
                return False

        return not increasing
