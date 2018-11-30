# https://leetcode.com/problems/design-tic-tac-toe/


class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board_size = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        piece = 1 if player == 1 else -1
        self.rows[row] += piece
        self.cols[col] += piece
        if row == col: self.diag += piece
        if row == self.board_size - col - 1: self.anti_diag += piece

        if piece * self.board_size in (self.rows[row], self.cols[col], self.diag, self.anti_diag):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
