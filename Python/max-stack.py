# https://leetcode.com/problems/max-stack/


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.s: self.s.append((x, x))
        else: self.s.append((x, max(x, self.s[-1][1])))

    def pop(self):
        """
        :rtype: int
        """
        return self.s.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.s[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        m = self.s[-1][1]
        t = []

        while self.s[-1][0] != m: t.append(self.pop())
        e = self.pop()
        for x in reversed(t): self.push(x)
        return e

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

