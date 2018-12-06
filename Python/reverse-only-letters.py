# https://leetcode.com/problems/reverse-only-letters/


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        l, r = 0, len(S) - 1
        S = list(S)
        while l < r:
            while l < r and not S[l].isalpha(): l += 1
            while r > l and not S[r].isalpha(): r -= 1
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        return ''.join(S)
