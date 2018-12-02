# https://leetcode.com/problems/number-of-boomerangs/


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def calc_sq_dist(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        boomerangs = 0
        for i in range(len(points)):
            sq_dist_map = {}
            for j in range(len(points)):
                if i == j: continue
                sq_dist = calc_sq_dist(points[i], points[j])
                if sq_dist not in sq_dist_map: sq_dist_map[sq_dist] = 0
                boomerangs += sq_dist_map[sq_dist] * 2
                sq_dist_map[sq_dist] += 1

        return boomerangs
