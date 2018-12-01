# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/


from heapq import *


class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = sorted((w / q, q, w) for q, w in zip(quality, wage))
        heap = []
        ans, sum_quality = float('inf'), 0

        for r, q, w in workers:
            heappush(heap, -q)
            sum_quality += q

            if len(heap) > K: sum_quality += heappop(heap)
            if len(heap) == K: ans = min(ans, r * sum_quality)

        return float(ans)
