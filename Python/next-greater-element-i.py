# https://leetcode.com/problems/next-greater-element-i/


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []
        for num in nums1:
            i = nums2.index(num)
            for j in range(i + 1, len(nums2)):
                if nums2[j] > num:
                    out.append(nums2[j])
                    break
            else:
                out.append(-1)
        return out

