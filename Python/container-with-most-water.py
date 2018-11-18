# https://leetcode.com/problems/container-with-most-water/


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water, i, j = 0, 0, len(height) - 1
        while i < j:
            h = min(height[i], height[j])
            water = max(water, h * (j - i))
            while i < j and height[i] <= h: i += 1
            while i < j and height[j] <= h: j -= 1
        return water
