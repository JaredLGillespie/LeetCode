# https://leetcode.com/problems/word-search/


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(row, col, index):
            if index == len(word): return True
            for nr, nc in neighbors(row, col):
                if board[nr][nc] == word[index]:
                    board[nr][nc] = ''
                    if search(nr, nc, index + 1): return True
                    board[nr][nc] = word[index]
            return False

        def neighbors(row, col):
            if row > 0: yield row - 1, col
            if row < num_rows - 1: yield row + 1, col
            if col > 0: yield row, col - 1
            if col < num_cols - 1: yield row, col + 1

        if not word: return True
        if not board: return False

        num_rows, num_cols = len(board), len(board[0])
        for row in range(num_rows):
            for col in range(num_cols):
                if word[0] == board[row][col]:
                    board[row][col] = ''
                    if search(row, col, 1): return True
                    board[row][col] = word[0]
        return False
