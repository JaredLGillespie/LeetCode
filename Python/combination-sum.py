# https://leetcode.com/problems/combination-sum/


class Solution(object):
    def combination_helper(self, candidates, target, index, comb, ans):
        if target == 0:
            ans.append(comb[:])
            return

        if index >= len(candidates):
            return

        self.combination_helper(candidates, target, index + 1, comb, ans)
        if candidates[index] <= target:
            comb.append(candidates[index])
            self.combination_helper(candidates, target - candidates[index], index, comb, ans)
            comb.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = list(sorted(candidates, reverse=True))
        ans = []
        self.combination_helper(candidates, target, 0, [], ans)
        return ans
