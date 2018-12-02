# https://leetcode.com/problems/line-reflection/


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points: return True
        X = min(points)[0] + max(points)[0]
        return len({(x, y) for x, y in points}.difference((X - x, y) for x, y in points)) == 0
