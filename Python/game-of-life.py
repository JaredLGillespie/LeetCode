# https://leetcode.com/problems/game-of-life/


class Solution:
    def count_live_neighbors(self, board, row, col):
        return sum(1 for r, c in self.get_neighbors(board, row, col) if board[r][c] > 0)

    def get_neighbors(self, board, row, col):
        if row > 0:
            yield row - 1, col
            if col > 0: yield row - 1, col - 1
            if col < len(board[0]) - 1: yield row - 1, col + 1

        if row < len(board) - 1:
            yield row + 1, col
            if col > 0: yield row + 1, col - 1
            if col < len(board[0]) - 1: yield row + 1, col + 1

        if col > 0: yield row, col - 1
        if col < len(board[0]) - 1: yield row, col + 1

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Simulate game: 0 -> dead, 1 -> live, -1 -> dead now alive, 2 -> alive now dead
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 1:
                    live_neighbors = self.count_live_neighbors(board, row, col)
                    # 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
                    if live_neighbors < 2: board[row][col] = 2
                    # 2. Any live cell with two or three live neighbors lives on to the next generation.
                    elif live_neighbors < 4: pass
                    # 3. Any live cell with more than three live neighbors dies, as if by over-population.
                    else: board[row][col] = 2
                else:
                    live_neighbors = self.count_live_neighbors(board, row, col)
                    # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if live_neighbors == 3: board[row][col] = -1

        # Fix board: -1 -> 1, 2 -> 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == -1: board[row][col] = 1
                if board[row][col] == 2: board[row][col] = 0
