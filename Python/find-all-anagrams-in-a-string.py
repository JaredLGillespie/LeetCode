# https://leetcode.com/problems/find-all-anagrams-in-a-string/


from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq = Counter(p)
        remaining_to_match = set(p)
        matching_chars = set(p)
        anagram_pos = []

        l, r = 0, 0

        while r < len(s):
            c = s[r]
            freq[c] -= 1
            if remaining_to_match and c in remaining_to_match and freq[c] == 0:
                remaining_to_match.remove(c)

            while not remaining_to_match and l < r and (s[l] not in matching_chars or freq[s[l]] < 0):
                freq[s[l]] += 1
                l += 1

            if not remaining_to_match and r - l + 1== len(p):
                anagram_pos.append(l)

            r += 1

        if not remaining_to_match and len(remaining_to_match) == len(p):
            anagram_pos.append(l)

        return anagram_pos
