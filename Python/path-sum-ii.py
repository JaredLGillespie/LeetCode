# https://leetcode.com/problems/path-sum-ii


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        if not root.left and not root.right:
            if sum == root.val:
                return [[root.val]]
            return []

        ret = []
        if root.left:
            for path in self.pathSum(root.left, sum - root.val):
                ret.append([root.val] + path)

        if root.right:
            for path in self.pathSum(root.right, sum - root.val):
                ret.append([root.val] + path)

        return ret
