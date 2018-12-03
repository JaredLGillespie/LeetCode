# https://leetcode.com/problems/contains-duplicate-iii/


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0: return False
        prev = {}
        bucket_width = t + 1
        for i in range(len(nums)):
            m = nums[i] // bucket_width
            if m in prev: return True
            if m - 1 in prev and abs(nums[i] - prev[m - 1]) < bucket_width: return True
            if m + 1 in prev and abs(nums[i] - prev[m + 1]) < bucket_width: return True
            prev[m] = nums[i]
            if i >= k: del prev[nums[i - k] // bucket_width]
        return False
