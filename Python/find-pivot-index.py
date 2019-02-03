# https://leetcode.com/problems/find-pivot-index/


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, sum(nums)

        for i, n in enumerate(nums):
            r -= n
            if l == r: return i
            l += n

        return -1
