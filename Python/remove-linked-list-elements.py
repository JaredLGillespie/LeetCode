# https://leetcode.com/problems/remove-linked-list-elements/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next

        if not head: return None

        node = head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return head
