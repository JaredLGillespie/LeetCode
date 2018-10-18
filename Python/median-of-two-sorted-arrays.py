# https://leetcode.com/problems/median-of-two-sorted-arrays


class Solution(object):
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1: return self.kth(A, B, l // 2)
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a: return b[k]
        if not b: return a[k]

        ia, ib = len(a) // 2, len(b) // 2

        if ia + ib < k:
            if a[ia] > b[ib]: return self.kth(a, b[ib + 1:], k - ib - 1)
            return self.kth(a[ia + 1:], b, k - ia - 1)

        if a[ia] > b[ib]: return self.kth(a[:ia], b, k)
        return self.kth(a, b[:ib], k)
