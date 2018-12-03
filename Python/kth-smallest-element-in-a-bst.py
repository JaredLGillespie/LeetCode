# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def search(root):
            nonlocal current_pos
            if not root: return float('inf')
            left = search(root.left)
            if left != float('inf'): return left
            current_pos += 1
            if current_pos == k: return root.val
            right = search(root.right)
            if right != float('inf'): return right
            return float('inf')

        current_pos = 0
        return search(root)
