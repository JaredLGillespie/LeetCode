# https://leetcode.com/problems/path-sum-iii/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def search(root, sums):
            if not root: return

            sums.append(0)
            for i in range(len(sums)):
                sums[i] += root.val
                if sums[i] == sum:
                    nonlocal total_sums
                    total_sums += 1

            search(root.left, sums)
            search(root.right, sums)

            for i in range(len(sums)):
                sums[i] -= root.val
            sums.pop()

        total_sums = 0
        search(root, [])
        return total_sums


def build_tree(root, index=0):
    if root is None: return None
    if index >= len(root): return None
    if root[index] is None: return None
    node = TreeNode(root[index])
    node.left = build_tree(root, index * 2 + 1)
    node.right = build_tree(root, index * 2 + 2)
    return node


root = [10,5,-3,3,2,None,11,3,-2,None,1]
sum = 8

tree = build_tree(root)
print(Solution().pathSum(tree, sum))
