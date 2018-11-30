# https://leetcode.com/problems/fruit-into-baskets/


class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree: return 0
        start_index, end_index = 0, len(tree) - 1

        max_collected_fruits = 0
        while start_index < end_index + 1:
            next_index, fruitA, fruitB = -1, -1, -1
            fruits_collected = 0
            for i in range(start_index, end_index + 1):
                if fruitA == -1:
                    fruits_collected += 1
                    fruitA = tree[i]
                elif fruitA == tree[i]:
                    fruits_collected += 1
                elif fruitB == -1:
                    fruits_collected += 1
                    fruitB = tree[i]
                elif fruitB == tree[i]:
                    fruits_collected += 1
                else:
                    max_collected_fruits = max(max_collected_fruits, fruits_collected)
                    if next_index == -1: start_index = end_index + 1
                    else: start_index = next_index
                    break

                if i > 0 and tree[i] != tree[i - 1]: next_index = i
            else: break

        max_collected_fruits = max(max_collected_fruits, fruits_collected)
        return max_collected_fruits
