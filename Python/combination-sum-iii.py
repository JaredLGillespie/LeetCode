# https://leetcode.com/problems/combination-sum-iii/


class Solution(object):
    def combination_helper(self, k, n, index, comb, ans):
        if k < 0: return
        if n == 0:
            if k == 0: ans.append(comb[:])
            return

        if index > 9: return

        for i in range(index, 10):
            comb.append(i)
            self.combination_helper(k - 1, n - i, i + 1, comb, ans)
            comb.pop()

    def combinationSum3(self, k, n):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.combination_helper(k, n, 1, [], ans)
        return ans
