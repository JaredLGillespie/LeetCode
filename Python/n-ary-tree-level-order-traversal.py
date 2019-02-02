# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        def traverse(root, level):
            if not root: return
            while len(ret) <= level:
                ret.append([])

            ret[level].append(root.val)
            for child in root.children:
                traverse(child, level + 1)

        ret = []
        traverse(root, 0)
        return ret
