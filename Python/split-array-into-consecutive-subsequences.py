# https://leetcode.com/problems/split-array-into-consecutive-subsequences/


from collections import Counter


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        remaining = Counter(nums)
        end = Counter()

        for num in nums:
            if remaining[num] == 0: continue
            remaining[num] -= 1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif remaining[num + 1] > 0 and remaining[num + 2] > 0:
                remaining[num + 1] -= 1
                remaining[num + 2] -= 1
                end[num + 2] += 1
            else: return False
        return True
