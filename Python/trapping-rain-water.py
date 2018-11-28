# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])

        water_trapped = current_height = 0
        for i in range(len(height)):
            if height[i] >= current_height: current_height = min(height[i], right[i])
            else: water_trapped += current_height - height[i]

        return water_trapped
