# https://leetcode.com/problems/number-complement/


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(['0' if x == '1' else '1' for x in bin(num)[2:]]))
