# https://leetcode.com/problems/roman-to-integer


m = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        highest = 1
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if m[c] == highest:
                num += m[c]
            elif m[c] > highest:
                highest = m[c]
                num += highest
            else:
                num -= m[c]
        return num
