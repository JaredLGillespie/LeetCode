# https://leetcode.com/problems/kth-largest-element-in-a-stream/


from heapq import *


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > self.k: heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heappush(self.heap, val)
        if len(self.heap) > self.k: heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
