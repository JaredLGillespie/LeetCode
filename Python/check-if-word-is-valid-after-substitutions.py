# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/


class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        na = nb = 0

        for c in S:
            if c == 'a':
                na += 1
            elif c == 'b':
                if na == 0:
                    return False
                nb += 1
                na -= 1
            else:
                if nb == 0:
                    return False
                nb -= 1

        return na == nb == 0

