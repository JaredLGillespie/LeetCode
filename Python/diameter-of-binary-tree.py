# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_diameter(root):
            if not root: return 0

            l = find_diameter(root.left)
            r = find_diameter(root.right)

            nonlocal diameter
            diameter = max(diameter, l + r)
            return max(l, r) + 1

        diameter = 0
        find_diameter(root)
        return diameter
