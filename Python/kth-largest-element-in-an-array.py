# https://leetcode.com/problems/kth-largest-element-in-an-array/


from heapq import *


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            if len(heap) < k: heappush(heap, num)
            else:
                num = max(num, heappop(heap))
                heappush(heap, num)
        return heap[0]
