# https://leetcode.com/problems/valid-tic-tac-toe-state/


class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        txs, tos = 0, 0
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X': txs += 1
                elif board[row][col] == 'O': tos += 1

        # Num Xs always == Os (or +1)
        if not (txs == tos or txs == tos + 1): return False

        xwp, owp = set(), set()
        for row in range(3):
            xs, os = 0, 0
            for col in range(3):
                if board[row][col] == 'X': xs += 1
                elif board[row][col] == 'O': os += 1
            if xs == 3: xwp.update((row, i) for i in range(3))
            if os == 3: owp.update((row, i) for i in range(3))

        for col in range(3):
            xs, os = 0, 0
            for row in range(3):
                if board[row][col] == 'X': xs += 1
                elif board[row][col] == 'O': os += 1
            if xs == 3: xwp.update((i, col) for i in range(3))
            if os == 3: owp.update((i, col) for i in range(3))

        if board[0][0] == board[1][1] == board[2][2] == 'X': xwp.update((i, i) for i in range(3))
        if board[0][0] == board[1][1] == board[2][2] == 'O': owp.update((i, i) for i in range(3))
        if board[0][2] == board[1][1] == board[2][0] == 'X': xwp.update((i, 2 - i) for i in range(3))
        if board[0][2] == board[1][1] == board[2][0] == 'O': owp.update((i, 2 - i) for i in range(3))

        # Xs and Os can't both win
        if xwp and owp: return False

        # Number of X winning positions should be <= 5 (could overlap 1 pos)
        if len(xwp) > 5: return False

        # Number of O winning positions should be <= 5 (could overlap 1 pos)
        if len(owp) > 5: return False

        # If X wins, must be more Xs than Os
        if xwp and txs <= tos: return False

        # If O wins, must be equal Xs as Os
        if owp and txs != tos: return False

        return True
