# https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return
        l, r = 0, len(nums) - 1

        while l < r:
            while l < r and nums[l] in (0, 1): l += 1
            while r > l and nums[r] == 2: r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        l = 0
        if nums[r] == 2: r -= 1
        while l < r:
            while l < r and nums[l] == 0: l += 1
            while r > l and nums[r] == 1: r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
