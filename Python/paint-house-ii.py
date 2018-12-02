# https://leetcode.com/problems/paint-house-ii/


class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(costs)):
            m1 = min(costs[i - 1])
            k = costs[i-1].index(m1)
            m2 = min(costs[i - 1][:k] + costs[i - 1][k + 1:])
            for j in range(len(costs[i])):
                costs[i][j] += m2 if j == k else m1

        return min(costs[-1]) if costs else 0
