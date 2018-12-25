# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target: l += 1
            elif numbers[l] + numbers[r] > target: r -= 1
            else: return l + 1, r + 1
