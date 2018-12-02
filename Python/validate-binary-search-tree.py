# https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate_branch(root, min, max):
            if root is None: return True
            if not (min < root.val < max): return False
            return validate_branch(root.right, root.val, max) and validate_branch(root.left, min, root.val)

        return validate_branch(root, -float('inf'), float('inf'))
