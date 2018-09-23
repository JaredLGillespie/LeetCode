# https://leetcode.com/problems/snakes-and-ladders

from collections import deque


class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        N2 = N*N

        queue = deque([1])
        visited = {1: 0}

        while queue:
            pos = queue.popleft()
            if pos == N2:
                return visited[pos]

            for other in range(pos + 1, min(pos + 6, N2) + 1):
                r, c = self.get_board_position(N, other)

                if board[r][c] != -1:
                    other = board[r][c]

                if other not in visited:
                    visited[other] = visited[pos] + 1
                    queue.append(other)

        return -1

    def get_board_position(self, N, p):
        row = N - 1 - (p - 1) // N
        if row % 2 == N % 2:
            col = N - 1 - (p - 1) % N
        else:
            col = (p - 1) % N
        return row, col
