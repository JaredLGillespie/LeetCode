# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        substring_chars = set()
        freq = {}
        longest_substring = 0
        while r < len(s):
            if s[r] not in freq: freq[s[r]] = 0
            freq[s[r]] += 1
            substring_chars.add(s[r])

            while len(substring_chars) > 2:
                freq[s[l]] -= 1
                if freq[s[l]] == 0: substring_chars.remove(s[l])
                l += 1

            r += 1
            longest_substring = max(longest_substring, r - l)

        longest_substring = max(longest_substring, r - l)
        return longest_substring
