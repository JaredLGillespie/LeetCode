# https://leetcode.com/problems/strobogrammatic-number/


class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l, r = 0, len(num) - 1
        while l < r:
            if num[l] == num[r] == '0': pass
            elif num[l] == num[r] == '8': pass
            elif num[l] == num[r] == '1': pass
            elif num[l] == '6' and num[r] == '9': pass
            elif num[l] == '9' and num[r] == '6': pass
            else: return False
            l += 1
            r -= 1

        if len(num) % 2 == 1: return num[len(num) // 2] in ('0', '8', '1')
        return True
