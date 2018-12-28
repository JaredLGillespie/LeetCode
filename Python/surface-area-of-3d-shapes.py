# https://leetcode.com/problems/surface-area-of-3d-shapes/


class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        surface_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0: continue
                surface_area += 2
                if row == 0: surface_area += grid[row][col]
                elif grid[row][col] > grid[row - 1][col]: surface_area += grid[row][col] - grid[row - 1][col]
                if row == len(grid) - 1: surface_area += grid[row][col]
                elif grid[row][col] > grid[row + 1][col]: surface_area += grid[row][col] - grid[row + 1][col]
                if col == 0: surface_area += grid[row][col]
                elif grid[row][col] > grid[row][col - 1]: surface_area += grid[row][col] - grid[row][col - 1]
                if col == len(grid[row]) - 1: surface_area += grid[row][col]
                elif grid[row][col] > grid[row][col + 1]: surface_area += grid[row][col] - grid[row][col + 1]

        return surface_area
