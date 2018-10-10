# https://leetcode.com/problems/valid-sudoku


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.is_valid_row(board, i):
                return False
            if not self.is_valid_col(board, i):
                return False

        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if not self.is_valid_box(board, row, col):
                    return False
        return True

    def is_valid_row(self, board, row):
        m = set()
        for col in range(9):
            v = board[row][col]
            if v == '.':
                continue

            if v in m:
                return False
            m.add(v)
        return True

    def is_valid_col(self, board, col):
        m = set()
        for row in range(9):
            v = board[row][col]
            if v == '.':
                continue

            if v in m:
                return False
            m.add(v)
        return True

    def is_valid_box(self, board, row, col):
        m = set()
        for r in range(3):
            for c in range(3):
                v = board[row + r][col + c]
                if v == '.':
                    continue

                if v in m:
                    return False
                m.add(v)
        return True
