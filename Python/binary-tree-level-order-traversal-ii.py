# https://leetcode.com/problems/binary-tree-level-order-traversal-ii


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        out = []
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.pop()

            if node:
                if len(out) < depth:
                    out.append([])
                out[depth - 1].append(node.val)
                queue.appendleft((node.left, depth + 1))
                queue.appendleft((node.right, depth + 1))
        return list(reversed(out))
