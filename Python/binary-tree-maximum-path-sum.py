# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def search(root):
            nonlocal max_path
            if not root: return 0
            max_path = max(max_path, root.val)

            left = search(root.left)
            right = search(root.right)
            max_path = max(max_path, left + root.val, right + root.val, left + right + root.val)
            return max(root.val, left + root.val, right + root.val)

        max_path = -float('inf')
        search(root)
        return max_path
