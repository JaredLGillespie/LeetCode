# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        for c in S:
            if c == '#':
                if s: s.pop()
            else: s.append(c)

        t = []
        for c in T:
            if c == '#':
                if t: t.pop()
            else: t.append(c)

        return ''.join(s) == ''.join(t)
