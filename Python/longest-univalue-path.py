# https://leetcode.com/problems/longest-univalue-path/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def search(root):
            l, r = 0, 0
            if root.left: l = search(root.left)
            if root.right: r = search(root.right)

            if root.left and root.left.val != root.val: l = 0
            if root.right and root.right.val != root.val: r = 0
            nonlocal longest_path
            longest_path = max(longest_path, l + r)
            return max(l, r) + 1

        longest_path = 0
        if root: search(root)
        return longest_path
