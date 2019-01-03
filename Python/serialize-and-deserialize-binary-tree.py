# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serialize_branch(root):
            if root is None: serialized.append('$')
            else:
                serialized.append(root.val)
                serialize_branch(root.left)
                serialize_branch(root.right)

        serialized = []
        serialize_branch(root)
        return '|'.join('$' if x is None else str(x) for x in serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def build_branch():
            if serialized[0] == '$':
                serialized.pop(0)
                return None
            node = TreeNode(int(serialized[0]))
            serialized.pop(0)
            node.left = build_branch()
            node.right = build_branch()
            return node

        if not data or data == '$': return None
        serialized = data.split('|')
        return build_branch()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
