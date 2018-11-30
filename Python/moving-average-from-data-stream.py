# https://leetcode.com/problems/moving-average-from-data-stream/


from collections import deque


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.elements = deque()
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.elements.append(val)
        self.sum += val

        if len(self.elements) > self.size:
            self.sum -= self.elements.popleft()

        return self.sum / len(self.elements)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
