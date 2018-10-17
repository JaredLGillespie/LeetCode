# https://leetcode.com/problems/pascals-triangle


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        if numRows == 1: return [[1]]

        out = [[1]]

        for i in range(0, numRows - 1):
            out.append([1] +
                       [out[-1][x] + out[-1][x + 1] for x in range(i)] +
                       [1])
        return out
