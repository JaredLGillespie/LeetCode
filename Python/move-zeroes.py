# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0

        while True:
            while r < len(nums) and nums[r] != 0: r += 1
            while l < len(nums) and (nums[l] == 0 or l < r): l += 1
            if l == len(nums) or r == len(nums): break
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
