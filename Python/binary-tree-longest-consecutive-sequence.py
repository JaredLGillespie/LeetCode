# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def search(root, prev, conseq):
            nonlocal lcs
            lcs = max(lcs, conseq)
            if not root: return
            else:
                if prev + 1 != root.val: conseq = 0
                search(root.left, root.val, conseq + 1)
                search(root.right, root.val, conseq + 1)

        lcs = 0
        search(root, -float('inf'), 0)
        return lcs
