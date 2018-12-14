# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(child) for child in root.children) + 1
