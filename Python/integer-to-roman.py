# https://leetcode.com/problems/integer-to-roman

m = [
    [1, 'I'],
    [4, 'IV'],
    [5, 'V'],
    [9, 'IX'],
    [10, 'X'],
    [40, 'XL'],
    [50, 'L'],
    [90, 'XC'],
    [100, 'C'],
    [400, 'CD'],
    [500, 'D'],
    [900, 'CM'],
    [1000, 'M']
]


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        out = []
        i = len(m) - 1
        while num:
            while m[i][0] > num:
                i -= 1
            out.append(m[i][1])
            num -= m[i][0]

        return ''.join(out)
