# https://leetcode.com/problems/inorder-successor-in-bst/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        ancestor = None
        while root and root.val:
            if p.val < root.val:
                ancestor = root
                root = root.left
            else:
                root = root.right
        return ancestor
