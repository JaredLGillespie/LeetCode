# https://leetcode.com/problems/dungeon-game/


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dungeon[m - 1][n - 1] = -min(0, dungeon[m - 1][n - 1])

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1: continue
                down = dungeon[row + 1][col] if row < m - 1 else float('inf')
                right = dungeon[row][col + 1] if col < n - 1 else float('inf')
                dungeon[row][col] = max(0, min(down, right) - dungeon[row][col])
        return dungeon[0][0] + 1

