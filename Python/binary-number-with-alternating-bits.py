# https://leetcode.com/problems/binary-number-with-alternating-bits/


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev_bit = -1

        while n > 0:
            cur_bit = n & 1
            if cur_bit == prev_bit: return False
            prev_bit = cur_bit
            n >>= 1

        return True
