# https://leetcode.com/problems/lonely-pixel-i/


class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        r = [0] * len(picture)
        c = [0] * len(picture[0])

        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == 'B':
                    r[row] += 1
                    c[col] += 1

        lp = 0
        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == 'B' and r[row] == c[col] == 1:
                    lp += 1

        return lp

print(Solution().findLonelyPixel([["W","W","B"],["W","B","W"],["B","W","W"]]))
