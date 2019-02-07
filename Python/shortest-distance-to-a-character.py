# https://leetcode.com/problems/shortest-distance-to-a-character/


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        out = [float('inf')] * len(S)
        dist = float('inf')

        for i in range(len(S)):
            if S[i] == C: dist = 0
            else: dist += 1
            out[i] = min(out[i], dist)

        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: dist = 0
            else: dist += 1
            out[i] = min(out[i], dist)

        return out
