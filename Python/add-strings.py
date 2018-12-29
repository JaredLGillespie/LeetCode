# https://leetcode.com/problems/add-strings/


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s = []
        c = 0
        i1, i2 = len(num1) - 1, len(num2) - 1

        while i1 >= 0 and i2 >= 0:
            n, c = c + int(num1[i1]) + int(num2[i2]), 0
            if n > 9: n, c = n % 10, 1
            s.append(n)
            i1, i2 = i1 - 1, i2 - 1

        while i1 >= 0:
            n, c = c + int(num1[i1]), 0
            if n > 9: n, c = n % 10, 1
            s.append(n)
            i1 -= 1

        while i2 >= 0:
            n, c = c + int(num2[i2]), 0
            if n > 9: n, c = n % 10, 1
            s.append(n)
            i2 -= 1

        if c > 0: s.append(1)
        return ''.join(map(str, reversed(s)))
