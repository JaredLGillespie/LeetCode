# https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import *


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head, tail = None, None
        heap = [(node.val, node) for node in lists if node]
        heapify(heap)

        while heap:
            _, node = heappop(heap)
            if node.next: heappush(heap, (node.next.val, node.next))
            if head is None: head = tail = node
            else: tail.next = tail = node

        return head
