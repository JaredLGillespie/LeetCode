# https://leetcode.com/problems/majority-element/


from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        return max([x for x in c], key=lambda x: c[x])
