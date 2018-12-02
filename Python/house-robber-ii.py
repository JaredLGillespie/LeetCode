# https://leetcode.com/problems/house-robber-ii/


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob_set(nums):
            a, b = 0, 0
            for num in nums:
                a, b = b, max(a + num, b)
            return b

        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        return max(rob_set(nums[:-1]), rob_set(nums[1:]))
