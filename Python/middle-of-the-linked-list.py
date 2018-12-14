# https://leetcode.com/problems/middle-of-the-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1, p2 = head, head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        return p1
