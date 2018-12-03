# https://leetcode.com/problems/closest-binary-search-tree-value/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        child = root.left if target < root.val else root.right
        if not child: return root.val
        child_val = self.closestValue(child, target)
        return min((root.val, child_val), key=lambda x: abs(target - x))
