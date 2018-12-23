# https://leetcode.com/problems/intersection-of-two-arrays-ii/


from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        f1 = Counter(nums1)
        out = []

        for num in nums2:
            if f1[num] > 0:
                out.append(num)
                f1[num] -= 1

        return out
