# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def search(root, memo):
            if root is None: return False
            if k - root.val in memo: return True
            memo.add(root.val)
            return search(root.left, memo) or search(root.right, memo)

        return search(root, set())
