# https://leetcode.com/problems/combination-sum-ii/


class Solution(object):
    def combination_helper(self, candidates, target, index, comb, ans):
        if target == 0:
            ans.append(comb[:])
            return

        if index >= len(candidates) or target < 0:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            comb.append(candidates[i])
            self.combination_helper(candidates, target - candidates[i], i + 1, comb, ans)
            comb.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = list(sorted(candidates, reverse=True))
        ans = []
        self.combination_helper(candidates, target, 0, [], ans)
        return ans
