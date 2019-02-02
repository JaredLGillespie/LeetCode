# https://leetcode.com/problems/n-ary-tree-preorder-traversal/


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def traverse(root):
            if not root: return
            ret.append(root.val)
            for child in root.children:
                traverse(child)

        ret = []
        traverse(root)
        return ret
