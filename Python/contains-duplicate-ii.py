# https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev = {}
        for i in range(len(nums)):
            if nums[i] not in prev or i - prev[nums[i]] > k: prev[nums[i]] = i
            else: return True
        return False
