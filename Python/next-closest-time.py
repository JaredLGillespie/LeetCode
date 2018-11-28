# https://leetcode.com/problems/next-closest-time/


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h, m = time.split(':')
        digits = h + m
        while True:
            if int(m) == 59: h, m = str(int(h) + 1), '00'
            else: m = str(int(m) + 1)
            if int(h) > 23: h = '00'
            if len(h) == 1: h = '0' + h
            if len(m) == 1: m = '0' + m
            if all(x in digits for x in h + m): return h + ':' + m
