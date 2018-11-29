# https://leetcode.com/problems/minimum-window-substring/


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        unique_chars = set(t)
        substring_freq = {}
        minimum_window = None

        for c in t:
            if c not in substring_freq:
                substring_freq[c] = 0
            substring_freq[c] += 1

        l, r = 0, 0
        while r < len(s):
            c = s[r]
            r += 1
            if c not in substring_freq: continue
            substring_freq[c] -= 1
            if substring_freq[c] > 0: continue
            if substring_freq[c] == 0: unique_chars.remove(c)
            if len(unique_chars) > 0: continue
            while l <= r:
                if s[l] not in substring_freq: l += 1
                elif substring_freq[s[l]] < 0:
                    substring_freq[s[l]] += 1
                    l += 1
                else: break

            if minimum_window is None or len(minimum_window) > r - l:
                minimum_window = s[l:r]

        return minimum_window if minimum_window else ''
