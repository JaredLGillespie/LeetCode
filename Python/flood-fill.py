# https://leetcode.com/problems/flood-fill/


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def fill(row, col, color):
            image[row][col] = newColor

            for nr, nc in neighbors(row, col):
                if image[nr][nc] == color:
                    fill(nr, nc, color)

        def neighbors(row, col):
            if row > 0: yield row - 1, col
            if row < len(image) - 1: yield row + 1, col
            if col > 0: yield row, col - 1
            if col < len(image[0]) - 1: yield row, col + 1

        if image[sr][sc] == newColor: return image
        fill(sr, sc, image[sr][sc])
        return image


print(Solution().floodFill([[0,0,0],[0,1,1]],1,1,1))
