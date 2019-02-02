# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


from collections import Counter


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        c = Counter(A)
        return [x for x in c if c[x] == len(A) // 2][0]
