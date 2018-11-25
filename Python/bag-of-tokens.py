# https://leetcode.com/problems/bag-of-tokens/


class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        max_points, current_points = 0, 0
        l, r = 0, len(tokens) - 1

        while l <= r:
            if tokens[l] <= P:
                current_points += 1
                P -= tokens[l]
                l += 1
            elif current_points == 0:
                break
            else:
                current_points -= 1
                P += tokens[r]
                r -= 1

            max_points = max(max_points, current_points)

        return max_points
