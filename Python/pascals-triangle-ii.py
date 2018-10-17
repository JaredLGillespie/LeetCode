# https://leetcode.com/problems/pascals-triangle-ii


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        out = [1]

        for i in range(0, rowIndex):
            out = ([1] +
                   [out[x] + out[x + 1] for x in range(i)] +
                   [1])
        return out
