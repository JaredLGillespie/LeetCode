# https://leetcode.com/problems/bomb-enemy/


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        mem = [[0] * len(grid[0]) for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'E': mem[row][col] = 1

        for row in range(len(grid)):
            s = 0
            for col in range(len(grid[0])):
                mem[row][col] += s
                if grid[row][col] == 'W': s = 0
                elif grid[row][col] == 'E': s += 1
            s = 0
            for col in range(len(grid[0]) - 1, -1, -1):
                mem[row][col] += s
                if grid[row][col] == 'W': s = 0
                elif grid[row][col] == 'E': s += 1

        for col in range(len(grid[0])):
            s = 0
            for row in range(len(grid)):
                mem[row][col] += s
                if grid[row][col] == 'W': s = 0
                elif grid[row][col] == 'E': s += 1
            s = 0
            for row in range(len(grid) - 1, -1, -1):
                mem[row][col] += s
                if grid[row][col] == 'W': s = 0
                elif grid[row][col] == 'E': s += 1

        max_enemies = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0': max_enemies = max(max_enemies, mem[row][col])

        return max_enemies
