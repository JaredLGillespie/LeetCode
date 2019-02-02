# https://leetcode.com/problems/1-bit-and-2-bit-characters/


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        ret = False
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                ret = False
                i += 2
            else:
                ret = True
                i += 1
        return ret
