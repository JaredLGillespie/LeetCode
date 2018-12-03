# https://leetcode.com/problems/missing-ranges/


class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper: return [str(lower)]
            else: return ['%s->%s' % (lower, upper)]

        out = []
        prev = lower - 1
        for num in nums + [upper + 1]:
            if num == prev: continue
            if num != prev + 1:
                if num == prev + 2: out.append(str(prev + 1))
                else: out.append('%s->%s' % (prev + 1, num - 1))
            prev = num

        return out
