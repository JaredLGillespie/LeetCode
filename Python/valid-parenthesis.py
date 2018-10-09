# https://leetcode.com/problems/valid-parentheses


from collections import deque


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()

        for c in s:
            if c == '(':  stack.append(')')
            elif c == '[':  stack.append(']')
            elif c == '{': stack.append('}')
            else:
                if not stack or stack.pop() != c:
                    return False

        return not stack
