# https://leetcode.com/problems/4sum


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        out = []
        i = 0
        while i < len(nums) - 3:
            for x in self.threeSum(nums, target - nums[i], i + 1):
                out.append([nums[i]] + x)

            i += 1
            while nums[i] == nums[i - 1]:
                i += 1
                if i >= len(nums) - 3:
                    break
            else:
                continue
            break

        return out

    def threeSum(self, nums, target, start_index):
        out = []
        i = start_index
        while i < len(nums) - 2:
            for x in self.twoSum(nums, target - nums[i], i + 1):
                out.append([nums[i]] + x)

            i += 1
            while nums[i] == nums[i - 1]:
                i += 1
                if i >= len(nums) - 2:
                    break
            else:
                continue
            break

        return out

    def twoSum(self, nums, target, start_index):
        out = []
        i, j = start_index, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                out.append([nums[i], nums[j]])

                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1

                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

        return out
