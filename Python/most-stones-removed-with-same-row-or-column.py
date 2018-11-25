# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


class Solution(object):
    def colorStones(self, stones, stone, colors, color):
        colors[stone] = color
        for i in range(len(stones)):
            if colors[i] != -1: continue
            if stones[i][0] == stones[stone][0] or stones[i][1] == stones[stone][1]:
                self.colorStones(stones, i, colors, color)

    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        colors = [-1] * len(stones)
        color = 0

        for i in range(len(stones)):
            if colors[i] == -1:
                self.colorStones(stones, i, colors, color)
                color += 1

        return len(stones) - color
