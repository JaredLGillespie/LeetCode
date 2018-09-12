# https://leetcode.com/problems/3sum


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        out = set()
        nums = sorted(nums)
        i = 0
        while i < len(nums) - 2:
            while i < len(nums) - 2 and nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2]:
                if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 0:
                    out.add((0, 0, 0))
                i += 1
            out.update(self.twoSum(nums, i + 1, nums[i]))
            i += 1
        return [list(i) for i in out]

    def twoSum(self, nums, ind, v):
        out = set()
        l, r = ind, len(nums) - 1

        while l < r:
            if v + nums[l] + nums[r] == 0:
                out.add((v, nums[l], nums[r]))
                l += 1
                r -= 1
            elif v + nums[l] + nums[r] < 0:
                l += 1
            else:
                r -= 1

        return out
