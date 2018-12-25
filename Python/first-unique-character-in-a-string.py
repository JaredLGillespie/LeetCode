# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = [float('inf')] * 26

        for i, c in enumerate(s):
            p = ord(c) - ord('a')
            if chars[p] == float('inf'): chars[p] = i
            else: chars[p] = -1

        m = float('inf')
        for i in chars:
            if i not in (-1, float('inf')):
                m = min(m, i)

        return m if m != float('inf') else -1
