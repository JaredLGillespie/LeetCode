# https://leetcode.com/problems/couples-holding-hands/


class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        def find_partner(index, partner):
            for j in range(index, len(row)):
                if row[j] == partner: return j

        swaps = 0
        for i in range(1, len(row), 2):
            if row[i] % 2 == 0 and row[i - 1] == row[i] + 1: continue
            if row[i] % 2 == 1 and row[i - 1] == row[i] - 1: continue
            if row[i] == row[i - 1]: continue
            pv = row[i - 1] + 1 if row[i - 1] % 2 == 0 else row[i - 1] - 1
            p = find_partner(i, pv)
            row[i], row[p] = row[p], row[i]
            swaps += 1
        return swaps
