# https://leetcode.com/problems/next-permutation/


class Solution(object):
    def swap(self, nums, i):
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break

    def reverse(self, nums, i):
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return;

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i - 1]: break

        if i > 0: self.swap(nums, i - 1)
        self.reverse(nums, i)
