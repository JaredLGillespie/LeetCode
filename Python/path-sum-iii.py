# https://leetcode.com/problems/path-sum-iii/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
