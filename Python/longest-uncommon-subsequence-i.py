# https://leetcode.com/problems/longest-uncommon-subsequence-i/


class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) > len(b): return len(a)
        if len(a) < len(b): return len(b)
        return len(a) if a != b else -1
