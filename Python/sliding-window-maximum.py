# https://leetcode.com/problems/sliding-window-maximum


from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        out = []
        window = deque()

        for i, n in enumerate(nums):
            while window and nums[window[-1]] < n:
                window.pop()

            window.append(i)
            if window[0] == i - k:
                window.popleft()

            if i >= k - 1:
                out.append(nums[window[0]])

        return out
