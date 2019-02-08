# https://leetcode.com/problems/increasing-order-search-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def search(root):
            nonlocal new_root, cur_root

            if root is None: return
            search(root.left)
            if new_root is None:
                new_root = cur_root = TreeNode(root.val)
            else:
                cur_root.right = TreeNode(root.val)
                cur_root = cur_root.right
            search(root.right)

        new_root = cur_root = None
        search(root)
        return new_root
