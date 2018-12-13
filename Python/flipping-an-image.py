# https://leetcode.com/problems/flipping-an-image/


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in range(len(A)):
            l, r = 0, len(A[0]) - 1
            while l < r:
                A[row][l], A[row][r] = A[row][r], A[row][l]
                l += 1
                r -= 1

        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col] ^= 1

        return A
