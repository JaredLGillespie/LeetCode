# https://leetcode.com/problems/logger-rate-limiter/


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.history = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.history or timestamp - self.history[message] >= 10:
            self.history[message] = timestamp
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
