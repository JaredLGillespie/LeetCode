# https://leetcode.com/problems/minimum-path-sum/description/


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0: dp[row][col] = grid[row][col]
                elif row == 0: dp[row][col] = grid[row][col] + dp[row][col - 1]
                elif col == 0: dp[row][col] = grid[row][col] + dp[row - 1][col]
                else: dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
        return dp[-1][-1]
