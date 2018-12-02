# https://leetcode.com/problems/design-hit-counter/


from collections import deque


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        self.hits.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
