# https://leetcode.com/problems/length-of-last-word


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s.strip():
            return 0

        return len(s.split()[-1])
