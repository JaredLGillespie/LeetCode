# https://leetcode.com/problems/number-of-distinct-islands/


class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def neighbors(row, col):
            if row > 0: yield row - 1, col
            if row < rows - 1: yield row + 1, col
            if col > 0: yield row, col - 1
            if col < cols - 1: yield row, col + 1

        def search(start_row, start_col, row, col, island):
            grid[row][col] = 0
            island.append(str(row * cols + col - (start_row * cols + start_col)))

            for nr, nc in neighbors(row, col):
                if grid[nr][nc] == 1:
                    search(start_row, start_col, nr, nc, island)

        islands = set()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    island = []
                    search(row, col, row, col, island)
                    islands.add('|'.join(island))

        return len(islands)
