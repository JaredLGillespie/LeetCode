# https://leetcode.com/problems/valid-word-square/


class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words): return False
                if i >= len(words[j]): return False
                if words[i][j] != words[j][i]: return False
        return True
