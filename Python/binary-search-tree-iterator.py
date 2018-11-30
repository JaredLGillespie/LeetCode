# https://leetcode.com/problems/binary-search-tree-iterator/


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#     def __repr__(self):
#         return str(self.val)


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.path = []
        while root:
            self.path.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.path) > 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.path.pop()
        node = ret.right
        while node:
            self.path.append(node)
            node = node.left

        return ret.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
