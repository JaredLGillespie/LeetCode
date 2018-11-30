# https://leetcode.com/problems/count-univalue-subtrees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def search(root):
            lu, lv = True, root.val
            ru, rv = True, root.val
            if root.left: lu, lv = search(root.left)
            if root.right: ru, rv = search(root.right)
            if not lu: return False, root.val
            if not ru: return False, root.val
            if not (lv == rv == root.val): return False, root.val

            nonlocal univalue_subtrees
            univalue_subtrees += 1
            return True, root.val

        univalue_subtrees = 0
        if root: search(root)
        return univalue_subtrees
