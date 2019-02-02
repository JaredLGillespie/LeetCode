# https://leetcode.com/problems/array-partition-i/


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(x for i, x in enumerate(sorted(nums)) if i & 1 == 0)
