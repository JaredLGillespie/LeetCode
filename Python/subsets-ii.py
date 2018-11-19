# https://leetcode.com/problems/subsets-ii/


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [[]]
        nums.sort()

        l = 1
        for i in range(len(nums)):
            if nums[i] != nums[i - 1]:
                l = len(out)

            for j in range(len(out) - l, len(out)):
                out.append(out[j] + [nums[i]])

        return out
