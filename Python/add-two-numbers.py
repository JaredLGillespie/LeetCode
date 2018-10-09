# https://leetcode.com/problems/add-two-numbers


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.get_num(l1)
        n2 = self.get_num(l2)
        return self.create_num(n1 + n2)

    def get_num(self, node):
        n = 0
        p = 1
        while node:
            n += node.val * p
            p *= 10
            node = node.next
        return n

    def create_num(self, num):
        if num == 0:
            return ListNode(0)

        head = None
        current = None
        while num > 0:
            num, r = divmod(num, 10)
            node = ListNode(r)
            if head is None:
                head = node
                current = node
            else:
                current.next = node
                current = node
        return head
