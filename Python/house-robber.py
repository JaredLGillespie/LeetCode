# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for num in nums:
            a, b = b, max(a + num, b)
        return b
