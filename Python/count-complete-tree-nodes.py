# https://leetcode.com/problems/count-complete-tree-nodes/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_height(root):
            if not root: return -1
            return get_height(root.left) + 1

        nodes, height = 0, get_height(root)
        while root:
            if get_height(root.right) == height - 1:
                nodes += 1 << height
                root = root.right
            else:
                nodes += 1 << height - 1
                root = root.left
            height -= 1
        return nodes
