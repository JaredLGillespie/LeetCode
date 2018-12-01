# https://leetcode.com/problems/heaters/


class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        left = [0] * len(houses)
        right = [0] * len(houses)

        houses.sort()
        heaters.sort()
        closest_heater = -float('inf')
        j = 0
        for i in range(len(houses)):
            while j < len(heaters) and heaters[j] <= houses[i]:
                closest_heater = heaters[j]
                j += 1
            left[i] = closest_heater

        closest_heater = float('inf')
        j = len(heaters) - 1
        for i in range(len(houses) - 1, -1, -1):
            while j > -1 and heaters[j] >= houses[i]:
                closest_heater = heaters[j]
                j -= 1
            right[i] = closest_heater

        warm_radius = 0
        for i in range(len(houses)):
            warm_radius = max(warm_radius, min(houses[i] - left[i], right[i] - houses[i]))

        return warm_radius
