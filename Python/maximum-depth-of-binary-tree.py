# https://leetcode.com/problems/maximum-depth-of-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.max_depth_branch(root.left, 1), self.max_depth_branch(root.right, 1))

    def max_depth_branch(self, root, depth):
        if not root:
            return depth

        return max(self.max_depth_branch(root.left, depth + 1), self.max_depth_branch(root.right, depth + 1))
