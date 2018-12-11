# https://leetcode.com/problems/palindrome-permutation/


class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        odds = 0
        freq = {}

        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
            if freq[c] % 2 == 1: odds += 1
            else: odds -= 1

        return n % 2 == odds == 0 or n % 2 == odds == 1
