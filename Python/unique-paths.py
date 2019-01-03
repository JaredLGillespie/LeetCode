# https://leetcode.com/problems/unique-paths/


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def search(x, y):
            if (x, y) in memo: return memo[x, y]
            if x >= m: return 0
            if y >= n: return 0

            paths = 0
            if x > 0: paths += search(x - 1, y)
            if y > 0: paths += search(x, y - 1)
            memo[(x, y)] = paths
            search(x + 1, y)
            search(x, y + 1)
            return paths

        memo = {(0, 0): 1}
        search(0, 1)
        search(1, 0)
        return memo[(m - 1, n - 1)]
