# https://leetcode.com/problems/repeated-string-match/


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        t, c = '', 0
        while len(t) < len(B):
            t += A
            c += 1
            if B in t: return c

        if B in t + A: return c + 1
        return - 1
