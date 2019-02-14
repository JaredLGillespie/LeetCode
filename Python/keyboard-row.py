# https://leetcode.com/problems/keyboard-row/


KEYS = {
    **{k:1 for k in 'QWERTYUIOP'},
    **{k:2 for k in 'ASDFGHJKL'},
    **{k:3 for k in 'ZXCVBNM'}
}


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [word for word in words if len({KEYS[k] for k in word.upper()}) == 1]
