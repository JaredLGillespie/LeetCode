# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0: return []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 1, len(matrix) - 1
        direction = 0  # 0 -> right, 1 -> down, 2 -> left, 3 -> up
        out = []
        row, col = 0, -1
        while True:
            if direction == 0:  # right
                if left > right: break
                col += 1
                while col < right:
                    out.append(matrix[row][col])
                    col += 1
                out.append(matrix[row][col])
                right -= 1

            elif direction == 1:  # down
                if top > bottom: break
                row += 1
                while row < bottom:
                    out.append(matrix[row][col])
                    row += 1
                out.append(matrix[row][col])
                bottom -= 1

            elif direction == 2:  # left
                if left > right: break
                col -= 1
                while col > left:
                    out.append(matrix[row][col])
                    col -= 1
                out.append(matrix[row][col])
                left += 1

            else:  # up
                if top > bottom: break
                row -= 1
                while row > top:
                    out.append(matrix[row][col])
                    row -= 1
                out.append(matrix[row][col])
                top += 1

            direction = (direction + 1) % 4

        return out
