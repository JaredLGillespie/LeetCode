# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                l = m - 1
                while l >= 0 and nums[l] == target:
                    l -= 1

                r = m + 1
                while r < len(nums) and nums[r] == target:
                    r += 1

                return [l + 1, r - 1]

            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return [-1, -1]
