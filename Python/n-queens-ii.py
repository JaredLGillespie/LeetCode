# https://leetcode.com/problems/n-queens-ii/


class Solution(object):
    def valid_pieces(self, n, pieces, current_piece):
        for i in range(n):
            if i == current_piece or pieces[i] == -1: continue
            if pieces[i] == pieces[current_piece]: return False
            if abs(i - current_piece) == abs(pieces[i] - pieces[current_piece]): return False

        return True

    def nqueens_helper(self, n, pieces, current_piece):
        if current_piece == n:
            return 1

        sols = 0
        for i in range(n):
            pieces[current_piece] = i
            if self.valid_pieces(n, pieces, current_piece):
                sols += self.nqueens_helper(n, pieces, current_piece + 1)
            pieces[current_piece] = -1
        return sols

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.nqueens_helper(n, [-1] * n, 0)
