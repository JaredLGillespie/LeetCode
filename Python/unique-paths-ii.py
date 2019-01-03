# https://leetcode.com/problems/unique-paths-ii/


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] != 1: obstacleGrid[0][0] = -1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1: continue
                paths = 0
                if row > 0: paths += min(0, obstacleGrid[row - 1][col])
                if col > 0: paths += min(0, obstacleGrid[row][col - 1])
                obstacleGrid[row][col] += paths

        return -obstacleGrid[-1][-1] if obstacleGrid[-1][-1] != 1 else 0
