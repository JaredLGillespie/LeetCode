# https://leetcode.com/problems/sort-array-by-parity/


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [a for a in A if a % 2 == 0] + [a for a in A if a % 2 == 1]
