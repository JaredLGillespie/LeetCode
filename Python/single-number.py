# https://leetcode.com/problems/single-number


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for num in nums:
            x ^= num
        return x
