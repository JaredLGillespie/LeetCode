# https://leetcode.com/problems/license-key-formatting/


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(s.upper() for s in S if s.isalnum())
        first_group = len(S) % K
        out = []

        is_first_group = first_group > 0

        i = 0
        for s in S:
            if is_first_group and i == first_group:
                is_first_group = False
                out.append('-')
                i = 0

            if is_first_group:
                out.append(s)
            else:
                out.append(s)
                if i == K - 1: out.append('-')

            i = (i + 1) % K

        if out and out[-1] == '-': out.pop()
        return ''.join(out)
