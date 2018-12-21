# https://leetcode.com/problems/max-consecutive-ones/


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = cur_ones = 0

        for n in nums:
            if n == 1: cur_ones += 1
            else:
                max_ones = max(max_ones, cur_ones)
                cur_ones = 0

        return max(max_ones, cur_ones)
