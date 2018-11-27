# https://leetcode.com/problems/cherry-pickup/


class Solution(object):
    def cherryPickupHelper(self, r1, c1, r2, c2, grid, n, memo):
        if (r1, c1, r2, c2) in memo: return memo[(r1, c1, r2, c2)]

        if n in (r1, c1, r2, c2): return -1
        if -1 in (grid[r1][c1], grid[r2][c2]): return -1
        if r1 == c1 == r2 == c2 == n - 1: return grid[-1][-1]

        best = max(
            self.cherryPickupHelper(r1 + 1, c1, r2 + 1, c2, grid, n, memo),
            self.cherryPickupHelper(r1 + 1, c1, r2, c2 + 1, grid, n, memo),
            self.cherryPickupHelper(r1, c1 + 1, r2 + 1, c2, grid, n, memo),
            self.cherryPickupHelper(r1, c1 + 1, r2, c2 + 1, grid, n, memo))

        if best == -1:
            res = -1
        else:
            if r1 == r2 and c1 == c2:
                res = best + grid[r1][c1]
            else:
                res = best + grid[r1][c1] + grid[r2][c2]

        memo[(r1, c1, r2, c2)] = res
        return res

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[-1][-1] == -1: return 0
        return max(0, self.cherryPickupHelper(0, 0, 0, 0, grid, len(grid), {}))


print(Solution().cherryPickup(
    [[0, -1, 1],
     [1, -1, 1],
     [1, 1, 1]]
))

print(Solution().cherryPickup(
    [[1,-1,1,-1,1,1,1,1,1,-1],
     [-1,1,1,-1,-1,1,1,1,1,1],
     [1,1,1,-1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1,1,1],
     [-1,1,1,1,1,1,1,1,1,1],
     [1,-1,1,1,1,1,-1,1,1,1],
     [1,1,1,-1,1,1,-1,1,1,1],
     [1,-1,1,-1,-1,1,1,1,1,1],
     [1,1,-1,-1,1,1,1,-1,1,-1],
     [1,1,-1,1,1,1,1,1,1,1]]
))

print(Solution().cherryPickup(
    [[1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1],
     [1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1]]
))
