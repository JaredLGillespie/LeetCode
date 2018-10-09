# https://leetcode.com/problems/3sum-closest


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best = float('inf')

        for i in range(len(nums) - 2):
            v = self.twoSumClosest(nums, target, nums[i], i + 1)
            if abs(v - target) < abs(best - target):
                best = v
        return best

    def twoSumClosest(self, nums, target, other_num, start_index):
        i, j = start_index, len(nums) - 1
        best = float('inf')

        while i < j:
            v = nums[i] + nums[j] + other_num
            if abs(v - target) < abs(best - target):
                best = v

            if v < target:
                i += 1
            else:
                j -= 1

        return best
