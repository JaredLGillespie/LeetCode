# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or k == 0: return 0
        longest_substring = 0
        unique_characters = 0
        characters = {}
        l, r = 0, 0

        while r < len(s):
            while r < len(s) and (unique_characters < k or s[r] in characters):
                if s[r] not in characters:
                    unique_characters += 1
                    characters[s[r]] = 0
                characters[s[r]] += 1
                r += 1

            longest_substring = max(longest_substring, r - l)

            if unique_characters == k:
                while l <= r and unique_characters == k:
                    characters[s[l]] -= 1
                    if characters[s[l]] == 0:
                        unique_characters -= 1
                        del characters[s[l]]
                    l += 1

        return longest_substring
