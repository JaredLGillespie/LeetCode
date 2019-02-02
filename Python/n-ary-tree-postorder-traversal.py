# https://leetcode.com/problems/n-ary-tree-postorder-traversal/


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def traverse(root):
            if not root: return
            for child in root.children:
                traverse(child)
            ret.append(root.val)

        ret = []
        traverse(root)
        return ret
