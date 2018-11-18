# https://leetcode.com/problems/di-string-match/


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l, r = 0, len(S)
        out = []
        if S[0] == 'I':
            out.append(l)
            l += 1
        else:
            out.append(r)
            r -= 1

        p = ''
        c = 0

        for x in S:
            if x == 'I':
                if p in ('', 'I'):
                    c += 1
                else:
                    for i in range(l + c - 1, l - 1, -1):
                        out.append(i)
                    l += c
                    c = 1
                p = 'I'
            else:
                if p in ('', 'D'):
                    c += 1
                else:
                    for i in range(r - c + 1, r + 1):
                        out.append(i)
                    r -= c
                    c = 1
                p = 'D'

        if p == 'I':
            for i in range(r - c + 1, r + 1):
                out.append(i)
        else:
            for i in range(l + c - 1, l - 1, -1):
                out.append(i)

        return out
