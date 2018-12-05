# https://leetcode.com/problems/flip-game/submissions/


class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        out = []
        for i in range(0, len(s) - 1):
            if s[i:i+2] == '++': out.append(s[:i] + '--' + s[i+2:])
        return out
