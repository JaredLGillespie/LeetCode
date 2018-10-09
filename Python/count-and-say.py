# https://leetcode.com/problems/count-and-say/description/


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ['1']
        for i in range(n - 1):
            s = self.countAndSayHelper(s)
        return ''.join(s)

    def countAndSayHelper(self, s):
        p = None
        c = 0
        o = []
        for i in range(len(s)):
            if p is None or s[i] == p:
                c += 1
            else:
                o.append(str(c))
                o.append(p)
                c = 1
            p = s[i]

        if p is not None:
            o.append(str(c))
            o.append(p)
        return o
