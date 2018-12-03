# https://leetcode.com/problems/utf-8-validation/


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            if data[i] & (1 << 7) == 0: i += 1
            elif data[i] & (1 << 7 | 1 << 6 | 1 << 5) == (1 << 7 | 1 << 6):
                if i + 1 >= len(data) or data[i + 1] & (1 << 7 | 1 << 6) != (1 << 7): return False
                i += 2
            elif data[i] & (1 << 7 | 1 << 6 | 1 << 5 | 1 << 4) == (1 << 7 | 1 << 6 | 1 << 5):
                if i + 1 >= len(data) or data[i + 1] & (1 << 7 | 1 << 6) != (1 << 7): return False
                if i + 2 >= len(data) or data[i + 2] & (1 << 7 | 1 << 6) != (1 << 7): return False
                i += 3
            elif data[i] & (1 << 7 | 1 << 6 | 1 << 5 | 1 << 4 | 1 << 3) == (1 << 7 | 1 << 6 | 1 << 5 | 1 << 4):
                if i + 1 >= len(data) or data[i + 1] & (1 << 7 | 1 << 6) != (1 << 7): return False
                if i + 2 >= len(data) or data[i + 2] & (1 << 7 | 1 << 6) != (1 << 7): return False
                if i + 3 >= len(data) or data[i + 3] & (1 << 7 | 1 << 6) != (1 << 7): return False
                i += 4
            else: return False
        return True
