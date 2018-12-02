# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r = 0, len(s) - 1
        s = list(s)
        vowels = set('aeiouAEIOU')
        while l < r:
            while l < r and s[l] not in vowels: l += 1
            while l < r and s[r] not in vowels: r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
