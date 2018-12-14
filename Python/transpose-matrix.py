# https://leetcode.com/problems/transpose-matrix/


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]: return []
        T = []

        for col in range(len(A[0])):
            T.append([A[r][col] for r in range(len(A))])
        return T
