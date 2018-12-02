# https://leetcode.com/problems/range-sum-query-2d-immutable/


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: self.rmq = None
        else:
            self.rmq = [[0] * (len(matrix[0]) + 1)] + [[0] + matrix[r] for r in range(len(matrix))]

            for row in range(1, len(matrix) + 1):
                for col in range(1, len(matrix[0]) + 1):
                    self.rmq[row][col] += self.rmq[row][col - 1]

            for col in range(1, len(matrix[0]) + 1):
                for row in range(1, len(matrix) + 1):
                    self.rmq[row][col] += self.rmq[row - 1][col]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.rmq: return 0
        return (self.rmq[row2 + 1][col2 + 1] -
                self.rmq[row2 + 1][col1] -
                self.rmq[row1][col2 + 1] +
                self.rmq[row1][col1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
