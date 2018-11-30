# https://leetcode.com/problems/find-median-from-data-stream/


from heapq import *


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_left = []
        self.heap_right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.heap_left, -num)
        heappush(self.heap_right, -heappop(self.heap_left))

        if len(self.heap_left) < len(self.heap_right):
            heappush(self.heap_left, -heappop(self.heap_right))

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.heap_left and not self.heap_right: return 0
        if len(self.heap_left) > len(self.heap_right): return -self.heap_left[0]
        return (-self.heap_left[0] + self.heap_right[0]) / 2

