# https://leetcode.com/problems/merge-intervals/


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return intervals

        intervals.sort(key=lambda x: (x.start, x.end))
        merged_intervals = []
        prev_interval = None

        for interval in intervals:
            if prev_interval is None:
                prev_interval = interval
            elif prev_interval.start <= interval.end and interval.start <= prev_interval.end:
                prev_interval = Interval(min(prev_interval.start, interval.start), max(prev_interval.end, interval.end))
            else:
                merged_intervals.append(prev_interval)
                prev_interval = interval

        merged_intervals.append(prev_interval)
        return merged_intervals
