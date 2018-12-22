# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(0, len(nums) - 1):
            x ^= i

        for n in nums:
            x ^= n

        return x
