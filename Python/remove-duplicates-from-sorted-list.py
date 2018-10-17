# https://leetcode.com/problems/remove-duplicates-from-sorted-list


# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
