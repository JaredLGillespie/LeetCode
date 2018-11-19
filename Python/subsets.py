# https://leetcode.com/problems/subsets/


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [[]]

        for i in range(len(nums)):
            new_out = []
            for o in out:
                new_out.append(o + [nums[i]])
            out.extend(new_out)
        return out
