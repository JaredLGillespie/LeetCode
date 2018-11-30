# https://leetcode.com/problems/number-of-islands/


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def search(row, col):
            grid[row][col] = '0'

            for nr, nc in neighbors(row, col):
                if grid[nr][nc] == '1':
                    search(nr, nc)

        def neighbors(row, col):
            if row > 0: yield row - 1, col
            if row < len(grid) - 1: yield row + 1, col
            if col > 0: yield row, col - 1
            if col < len(grid[0]) - 1: yield row, col + 1

        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    num_islands += 1
                    search(row, col)
        return num_islands
