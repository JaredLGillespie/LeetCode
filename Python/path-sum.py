# https://leetcode.com/problems/path-sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return sum - root.val == 0

        return (root.left is not None and self.hasPathSum(root.left, sum - root.val)) or \
               (root.right is not None and self.hasPathSum(root.right, sum - root.val))
