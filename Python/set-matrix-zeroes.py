# https://leetcode.com/problems/set-matrix-zeroe


class Solution:
    def setZeroes(self, matrix):
        n = len(matrix)
        if n == 0:
            return matrix

        m = len(matrix[0])
        if m == 0:
            return matrix

        upper_left_is_zero = matrix[0][0] == 0
        row_zero_is_zero = any(True for i in range(m) if matrix[0][i] == 0)
        col_zero_is_zero = any(True for i in range(n) if matrix[i][0] == 0)

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_zero_is_zero or upper_left_is_zero:
            for i in range(m):
                matrix[0][i] = 0

        if col_zero_is_zero or upper_left_is_zero:
            for i in range(n):
                matrix[i][0] = 0


a = [
    [1], [0]
]

Solution().setZeroes(a)
print(a)

