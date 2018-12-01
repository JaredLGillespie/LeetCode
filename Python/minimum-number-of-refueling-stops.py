# https://leetcode.com/problems/minimum-number-of-refueling-stops/


from heapq import *


class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        heap = []
        res, i = 0, 0
        current_fuel = startFuel
        while current_fuel < target:
            while i < len(stations) and stations[i][0] <= current_fuel:
                heappush(heap, -stations[i][1])
                i += 1
            if not heap: return -1
            current_fuel += -heappop(heap)
            res += 1
        return res
