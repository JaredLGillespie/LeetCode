# https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/


# Definition for a Node.
# class Node(object):
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next


class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        node = Node(insertVal, head)
        if not head: return node

        cur, prev = head.next, head

        while True:
            if prev.val <= node.val <= cur.val: break
            if prev.val > cur.val and (node.val < cur.val or node.val > prev.val): break
            if cur == head: break
            cur, prev = cur.next, prev.next

        prev.next = node
        node.next = cur
        return head
