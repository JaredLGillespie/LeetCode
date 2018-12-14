# https://leetcode.com/problems/uncommon-words-from-two-sentences/


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        f = {}
        for a in A.split():
            if a not in f: f[a] = 0
            f[a] += 1

        for b in B.split():
            if b not in f: f[b] = 0
            f[b] += 1

        return list(k for k, v in f.items() if v == 1)
