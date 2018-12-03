# https://leetcode.com/problems/search-in-a-binary-search-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None: return None
        if root.val == val: return root
        if root.val < val: return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)
