# https://leetcode.com/problems/longest-palindromic-substring


class Solution:
    def longestPalindrome(self, s):
        if not s or len(s) == 1: return s
        min_start, max_len = 0, 1

        i = 0
        while i < len(s):
            if len(s) - i <= max_len / 2: break
            j, k = i, i
            while k < len(s) - 1 and s[k + 1] == s[k]:
                k += 1

            i = k + 1

            while k < len(s) - 1 and j > 0 and s[k + 1] == s[j - 1]:
                k += 1
                j -= 1

            new_len = k - j + 1
            if new_len > max_len:
                min_start = j
                max_len = new_len

        return s[min_start:min_start+max_len]
