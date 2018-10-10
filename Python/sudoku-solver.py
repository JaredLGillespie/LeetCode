# https://leetcode.com/problems/sudoku-solve


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve_sudoku_helper(board)

    def solve_sudoku_helper(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    digits = self.get_valid_digits(board, row, col)
                    if digits is None:
                        return False
                    for digit in digits:
                        board[row][col] = digit
                        if self.solve_sudoku_helper(board):
                            return True
                        board[row][col] = '.'
                    return False
        return self.is_complete(board)

    def is_complete(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    return False
        return True

    def get_valid_digits(self, board, row, col):
        valid_digits = set('123456789')
        valid_digits.difference_update(self.invalid_digits_from_row(board, row))
        valid_digits.difference_update(self.invalid_digits_from_col(board, col))
        valid_digits.difference_update(self.invalid_digits_from_box(board, (row // 3) * 3, (col // 3) * 3))
        return valid_digits

    def invalid_digits_from_row(self, board, row):
        m = set()
        for col in range(9):
            v = board[row][col]
            if v == '.':
                continue
            m.add(v)
        return m

    def invalid_digits_from_col(self, board, col):
        m = set()
        for row in range(9):
            v = board[row][col]
            if v == '.':
                continue
            m.add(v)
        return m

    def invalid_digits_from_box(self, board, row, col):
        m = set()
        for r in range(3):
            for c in range(3):
                v = board[row + r][col + c]
                if v == '.':
                    continue
                m.add(v)
        return m
