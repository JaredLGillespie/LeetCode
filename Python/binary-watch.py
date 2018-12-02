# https://leetcode.com/problems/binary-watch/


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def count_bits(x):
            bits = 0
            while x > 0:
                if x & 1: bits += 1
                x >>= 1
            return bits

        possible_times = []
        hours = 0
        while hours < 12:
            hb = count_bits(hours)
            minutes = 0
            while minutes < 60:
                mb = count_bits(minutes)
                if hb + mb == num:
                    possible_times.append('%s:%s' % (str(hours), str(minutes).rjust(2, '0')))
                minutes += 1
            hours += 1
        return possible_times
