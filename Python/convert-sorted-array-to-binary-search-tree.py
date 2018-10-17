# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        return self.sub_tree(nums, 0, len(nums) - 1)

    def sub_tree(self, nums, l, r):
        if l == r:
            return TreeNode(nums[l])
        if l > r:
            return TreeNode('null')

        m = (l + r) // 2
        node = TreeNode(nums[m])
        node.left = self.sub_tree(nums, l, m - 1)
        node.right = self.sub_tree(nums, m + 1, r)
        return node
