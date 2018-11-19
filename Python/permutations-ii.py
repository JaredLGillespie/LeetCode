# https://leetcode.com/problems/permutations-ii/


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [[]]

        for i in range(len(nums)):
            new_out = []
            for o in out:
                for j in range(i + 1):
                    new_out.append(o[:j] + [nums[i]] + o[j:])
                    if j < len(o) and o[j] == nums[i]: break
            out = new_out
        return out
