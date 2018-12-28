# https://leetcode.com/problems/excel-sheet-column-number/


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for c in s:
            n *= 26
            n += 1 + ord(c) - ord('A')

        return n
