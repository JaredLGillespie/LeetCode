# https://leetcode.com/problems/merge-sorted-array


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        k = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[k] = nums2[p2]
                p2 -= 1
            else:
                nums1[k] = nums1[p1]
                p1 -= 1
            k -= 1

        while p2 >= 0:
            nums1[k] = nums2[p2]
            p2 -= 1
            k -= 1
