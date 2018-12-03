# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def search(node):
            nonlocal res
            if not node: return
            if root.val < node.val < res: res = node.val
            search(node.left)
            search(node.right)

        res = float('inf')
        search(root)
        return res if res != float('inf') else -1
