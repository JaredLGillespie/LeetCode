# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        mapped_chars = set()
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in mapped_chars: return False
                mapping[s[i]] = t[i]
                mapped_chars.add(t[i])
            elif mapping[s[i]] != t[i]: return False
        return True
