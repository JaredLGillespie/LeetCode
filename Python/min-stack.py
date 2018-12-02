# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m = x if not self.stack else min(self.stack[-1][0], x)
        self.stack.append((m, x))

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()[1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
