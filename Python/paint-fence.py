# https://leetcode.com/problems/paint-fence/


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        same, diff = 0, k
        for _ in range(1, n):
            same, diff = diff, (same + diff) * (k - 1)
        return same + diff
