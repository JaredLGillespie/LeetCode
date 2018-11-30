# https://leetcode.com/problems/path-sum-iv/


class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def tree_pos(d, p):
            t, r = 0, 1
            for i in range(0, d - 1):
                t += r
                r *= 2
            return t + p - 1

        def search(index, sum):
            left_index = index * 2 + 1
            right_index = index * 2 + 2
            left_exists = left_index < MAX_TREE_SIZE and tree[left_index] is not None
            right_exists = right_index < MAX_TREE_SIZE and tree[right_index] is not None
            if left_exists: search(left_index, sum + tree[index])
            if right_exists: search(right_index, sum + tree[index])
            if not left_exists and not right_exists:
                nonlocal sums
                sums += sum + tree[index]

        MAX_TREE_SIZE = 15
        tree = [None] * MAX_TREE_SIZE
        for num in nums:
            d = num // 100
            p = (num % 100) // 10
            v = num % 10
            tp = tree_pos(d, p)
            tree[tp] = v

        sums = 0
        if tree[0] is not None: search(0, 0)
        return sums


nums = [113, 221]
print(Solution().pathSum(nums))
