# https://leetcode.com/problems/n-queens/


class Solution(object):
    def create_solution(self, n, pieces):
        sol = []
        for i in range(n):
            sol.append(''.join(['.'] * pieces[i] + ['Q'] + ['.'] * (n - pieces[i] - 1)))
        return sol

    def valid_pieces(self, n, pieces, current_piece):
        for i in range(n):
            if i == current_piece or pieces[i] == -1: continue
            if pieces[i] == pieces[current_piece]: return False
            if abs(i - current_piece) == abs(pieces[i] - pieces[current_piece]): return False

        return True

    def nqueens_helper(self, n, pieces, current_piece, sols):
        if current_piece == n:
            sols.append(self.create_solution(n, pieces))
            return

        for i in range(n):
            pieces[current_piece] = i
            if self.valid_pieces(n, pieces, current_piece):
                self.nqueens_helper(n, pieces, current_piece + 1, sols)
            pieces[current_piece] = -1

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        sols = []
        pieces = [-1] * n
        self.nqueens_helper(n, pieces, 0, sols)
        return sols
