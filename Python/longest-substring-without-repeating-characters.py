# https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        chars = {s[0]}
        longest_length = 1
        l, r = 0, 0

        while r < len(s) - 1:
            while s[r + 1] in chars:
                chars.remove(s[l])
                l += 1
            r += 1
            chars.add(s[r])
            longest_length = max(longest_length, r - l + 1)
        return longest_length
