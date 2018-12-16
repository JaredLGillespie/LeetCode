# https://leetcode.com/problems/average-of-levels-in-binary-tree/


from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return []
        queue = deque([(0, root)])
        prev_level = 0
        level_count = 1
        level_sum = 0
        averages = []

        while queue:
            level, node = queue.popleft()

            if level != prev_level:
                averages.append(level_sum / level_count)
                prev_level = level
                level_count = len(queue) + 1
                level_sum = 0

            level_sum += node.val

            if node.left:
                queue.append((level + 1, node.left))

            if node.right:
                queue.append((level + 1, node.right))

        averages.append(level_sum / level_count)
        return averages
