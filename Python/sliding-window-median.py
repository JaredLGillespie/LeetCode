# https://leetcode.com/problems/sliding-window-median/


from bisect import *


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        medians = []
        window = []
        for i in range(len(nums)):
            if i >= k: window.pop(bisect(window, nums[i - k]) - 1)
            insort(window, nums[i])
            if i >= k - 1: medians.append((window[k // 2] + window[(k - 1) // 2]) / 2)

        return medians
