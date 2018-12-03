# https://leetcode.com/problems/max-points-on-a-line/


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


from fractions import Fraction


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_points = 0 if not points else 1
        for i in range(len(points)):
            same_points, inf_points = 0, 0
            history = {}
            for j in range(i + 1, len(points)):
                pointA, pointB = points[i], points[j]
                if pointA.x == pointB.x and pointA.y == pointB.y: same_points = max(same_points, 1) + 1
                elif pointA.x == pointB.x: inf_points = max(inf_points, 1) + 1
                else:
                    slope = Fraction(pointA.y - pointB.y, pointA.x - pointB.x)
                    if slope in history: history[slope] += 1
                    else: history[slope] = 2
            max_points = max(max_points,
                             same_points,
                             inf_points + max(0, same_points - 1),
                             max(0, 0, *history.values()) + max(0, same_points - 1))
        return max_points
