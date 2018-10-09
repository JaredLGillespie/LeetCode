# https://leetcode.com/problems/generate-parentheses


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        memo = {}
        return self.generateParenthesis_helper(n * 2, 0, memo)

    def generateParenthesis_helper(self, n, l, memo):
        if (n, l) in memo:
            return memo[(n, l)]

        if n == 0:
            return ['']

        out = []

        if l > 0:
            for p in self.generateParenthesis_helper(n - 1, l - 1, memo):
                out.append(')' + p)

        if n > l:
            for p in self.generateParenthesis_helper(n - 1, l + 1, memo):
                out.append('(' + p)

        memo[(n, l)] = out
        return out

print(Solution().generateParenthesis(3))
