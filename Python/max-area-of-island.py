# https://leetcode.com/problems/max-area-of-island/


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def search(row, col):
            grid[row][col] = 0
            area = 1
            for nr, nc in neighbors(row, col):
                if grid[nr][nc] == 1:
                    area += search(nr, nc)
            return area

        def neighbors(row, col):
            if row > 0: yield row - 1, col
            if row < len(grid) - 1: yield row + 1, col
            if col > 0: yield row, col - 1
            if col < len(grid[0]) - 1: yield row, col + 1

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, search(row, col))
        return max_area
