# https://leetcode.com/problems/fair-candy-swap/


class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sa, sb = sum(A), sum(B)
        setb = set(B)
        for x in A:
            if x + (sb - sa) // 2 in setb:
                return x, x + (sb - sa) // 2
