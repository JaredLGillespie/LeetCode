# https://leetcode.com/problems/copy-list-with-random-pointer/


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        def get_cloned_node(node):
            if not node: return None
            if node in visited: return visited[node]
            else:
                visited[node] = RandomListNode(node.label)
                return visited[node]

        if not head: return None
        visited = {}

        new_head = new_node = get_cloned_node(head)
        new_head.random = get_cloned_node(head.random)
        node = head

        while node:
            new_node.next = get_cloned_node(node.next)
            new_node.random = get_cloned_node(node.random)
            new_node = new_node.next
            node = node.next

        return new_head
