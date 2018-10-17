# https://leetcode.com/problems/balanced-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_balanced_helper(root)[0]

    def is_balanced_helper(self, root):
        if not root:
            return True, 0

        left_balanced, left_depth = self.is_balanced_helper(root.left)

        if not left_balanced:
            return False, left_depth + 1

        right_balanced, right_depth = self.is_balanced_helper(root.right)

        if not right_balanced:
            return False, right_depth + 1

        if abs(left_depth - right_depth) > 1:
            return False, max(left_depth, right_depth) + 1

        return True, max(left_depth, right_depth) + 1
