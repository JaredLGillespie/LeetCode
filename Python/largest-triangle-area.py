# https://leetcode.com/problems/largest-triangle-area/


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    max_area = max(max_area, 0.5 * abs(points[i][0] * points[j][1] +
                                                       points[j][0] * points[k][1] +
                                                       points[k][0] * points[i][1] -
                                                       points[i][1] * points[j][0] -
                                                       points[j][1] * points[k][0] -
                                                       points[k][1] * points[i][0]))
        return max_area
