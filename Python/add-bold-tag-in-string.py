# https://leetcode.com/problems/add-bold-tag-in-string/


class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        intervals = []
        for i in range(len(s)):
            for d in dict:
                if s[i:i + len(d)] == d:
                    intervals.append([i, i + len(d) - 1])

        if not intervals: return s
        merged_intervals = []
        previous_interval = intervals[0]

        for interval in intervals:
            if (previous_interval[0] <= interval[0] <= previous_interval[1] or
                interval[0] <= previous_interval[1] <= interval[1] or
                previous_interval[0] == interval[1] + 1 or
                interval[0] == previous_interval[1] + 1):
                previous_interval = [min(interval[0], previous_interval[0]), max(interval[1], previous_interval[1])]
            else:
                merged_intervals.append(previous_interval)
                previous_interval = interval

        merged_intervals.append(previous_interval)

        interval_index = 0
        out = []

        for i, c in enumerate(s):
            if interval_index < len(merged_intervals):
                if i == merged_intervals[interval_index][0] == merged_intervals[interval_index][1]:
                    out.append('<b>')
                    out.append(c)
                    out.append('</b>')
                    interval_index += 1
                elif i == merged_intervals[interval_index][0]:
                    out.append('<b>')
                    out.append(c)
                elif i == merged_intervals[interval_index][1]:
                    out.append(c)
                    out.append('</b>')
                    interval_index += 1
                else:
                    out.append(c)
            else:
                out.append(c)

        return ''.join(out)
