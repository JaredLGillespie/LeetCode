# https://leetcode.com/problems/3sum-smaller/


class Solution:
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twoSumSmaller(index, target):
            triplets = 0
            l, r = index, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    triplets += r - l
                    l += 1
                else:
                    r -= 1
            return triplets

        nums.sort()
        triplets = 0
        for i in range(len(nums) - 2):
            triplets += twoSumSmaller(i + 1, target - nums[i])
        return triplets
