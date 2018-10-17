# https://leetcode.com/problems/symmetric-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.is_same(root.left, root.right)

    def is_same(self, a, b):
        if (a and not b) or (not a and b):
            return False

        if a and b:
            return a.val == b.val and self.is_same(a.left, b.right) and self.is_same(a.right, b.left)

        return True
