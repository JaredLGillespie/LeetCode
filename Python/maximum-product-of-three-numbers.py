# https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')

        for n in nums:
            if n <= min1: min1, min2 = n, min1
            elif n <= min2: min2 = n
            if n >= max1: max1, max2, max3 = n, max1, max2
            elif n >= max2: max2, max3 = n, max2
            elif n >= max3: max3 = n

        return max(min1 * min2 * max1, max1 * max2 * max3)
