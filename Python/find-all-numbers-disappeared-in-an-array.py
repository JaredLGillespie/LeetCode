# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        target = 1
        for n in sorted(nums):
            if n > target:
                out.extend(range(target, n))
                target = n + 1
            else:
                target = n + 1

        if target <= len(nums):
            out.extend(range(target, len(nums) + 1))

        return out
