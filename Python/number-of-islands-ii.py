# https://leetcode.com/problems/number-of-islands-ii/


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def neighbors(row, col):
            if row > 0 and grid[row - 1][col] == 1: yield row - 1, col
            if row < m - 1 and grid[row + 1][col] == 1: yield row + 1, col
            if col > 0 and grid[row][col - 1] == 1: yield row, col - 1
            if col < n - 1 and grid[row][col + 1] == 1: yield row, col + 1

        def find(x):
            p = parents[x]
            while p != x:
                x, p = p, parents[p]
            return p

        def union(x, y):
            px = find(x)
            py = find(y)
            if ranks[px] > ranks[py]: parents[py] = px
            elif ranks[px] < ranks[py]: parents[px] = py
            elif px == py:
                parents[py] = px
                ranks[px] += 1

            parents[find(y)] = find(x)

        parents = {i:i for i in range(m * n)}
        ranks = {i:0 for i in range(m * n)}
        grid = [[0] * n for _ in range(m)]

        out = []
        num_islands = 0
        for row, col in positions:
            grid[row][col] = 1
            p1 = row * n + col
            num_islands += 1
            neighs = list(neighbors(row, col))
            num_islands -= len({find(nr * n + nc) for nr, nc in neighs})
            for nr, nc in neighs:
                p2 = nr * n + nc
                union(p1, p2)
            out.append(num_islands)

        return out
