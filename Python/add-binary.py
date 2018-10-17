# https://leetcode.com/problems/add-binary


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return '{0:b}'.format(int(a, 2) + int(b, 2))
