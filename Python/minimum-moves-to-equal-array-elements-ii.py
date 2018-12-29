# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(abs(nums[len(nums) // 2] - n) for n in nums)

