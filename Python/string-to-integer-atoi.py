# https://leetcode.com/problems/string-to-integer-atoi


INT_MAX = 2**31 - 1
INT_MIN = -2**31


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        neg = 1
        num = 0
        for i in range(len(str)):
            c = str[i]
            if i == 0 and c == '-':
                neg = -1
            elif i == 0 and c == '+':
                continue
            elif c.isdigit():
                num = num * 10 + int(c)

                if neg == - 1and -num < INT_MIN:
                    return INT_MIN
                if neg == 1 and num > INT_MAX:
                    return INT_MAX
            else:
                break
        return num * neg
