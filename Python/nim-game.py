# https://leetcode.com/problems/nim-game/


class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
