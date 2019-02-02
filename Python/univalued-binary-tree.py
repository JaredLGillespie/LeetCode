# https://leetcode.com/problems/univalued-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def search(root, v):
            if root is None: return True
            if root.val != v: return False
            return search(root.left, v) and search(root.right, v)

        if not root: return True
        return search(root, root.val)
