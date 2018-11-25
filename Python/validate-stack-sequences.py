# https://leetcode.com/problems/validate-stack-sequences/


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pop_index = 0

        for x in pushed:
            stack.append(x)

            while stack and stack[-1] == popped[pop_index]:
                pop_index += 1
                stack.pop()

        return pop_index == len(popped)
