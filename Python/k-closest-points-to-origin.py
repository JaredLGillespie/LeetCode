# https://leetcode.com/problems/k-closest-points-to-origin/


from heapq import *


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []

        for p in points:
            heappush(heap, (-(p[0]**2 + p[1]**2), p))
            if len(heap) > K: heappop(heap)

        return [p[1] for p in heap]

