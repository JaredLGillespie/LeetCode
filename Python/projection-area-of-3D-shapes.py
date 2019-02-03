# https://leetcode.com/problems/projection-area-of-3d-shapes/


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        x, y, z = 0, 0, 0

        for r in range(n):
            max_y, max_z = 0, 0
            for c in range(n):
                if grid[r][c] > 0: x += 1
                max_y = max(max_y, grid[r][c])
                max_z = max(max_z, grid[c][r])
            y += max_y
            z += max_z

        return x + y + z
