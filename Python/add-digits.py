# https://leetcode.com/problems/add-digits/


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9
