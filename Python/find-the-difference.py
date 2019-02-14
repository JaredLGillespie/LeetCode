# https://leetcode.com/problems/find-the-difference/


from collections import Counter


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sc = Counter(s)
        tc = Counter(t)

        for c in tc:
            if tc[c] > sc[c]:
                return c
