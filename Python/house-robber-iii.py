# https://leetcode.com/problems/house-robber-iii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recurse(root):
            plv = lv = prv = rv = 0
            if root.left: plv, lv = recurse(root.left)
            if root.right: prv, rv = recurse(root.right)
            return lv + rv, max(root.val + plv + prv, lv + rv)

        return max(recurse(root)) if root else 0


