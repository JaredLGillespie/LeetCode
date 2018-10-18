# https://leetcode.com/problems/linked-list-cycle-ii


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head.next
            fast = head.next.next

            while slow != fast:
                slow = slow.next
                fast = fast.next.next

            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        except AttributeError:
            return None
