# https://leetcode.com/problems/permutations/


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [[]]

        for i in range(len(nums)):
            new_out = []
            for j in range(i + 1):
                for o in out:
                    new_out.append(o[:j] + [nums[i]] + o[j:])
            out = new_out
        return out
