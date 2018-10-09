# https://leetcode.com/problems/two-sum


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i, n in enumerate(nums):
            if (target - n) in m:
                return [m[target - n], i]
            m[n] = i
