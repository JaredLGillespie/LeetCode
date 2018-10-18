# https://leetcode.com/problems/single-number-ii


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a
        return a
