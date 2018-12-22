# https://leetcode.com/problems/baseball-game/


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        return sum(stack)
