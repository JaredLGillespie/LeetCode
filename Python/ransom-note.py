# https://leetcode.com/problems/ransom-note/


from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        available = Counter(magazine)

        for c in ransomNote:
            if available[c] <= 0: return False
            available[c] -= 1
        return True
