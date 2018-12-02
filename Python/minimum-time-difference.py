# https://leetcode.com/problems/minimum-time-difference/


class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert_to_minutes(x):
            h, m = map(int, x.split(':'))
            return h * 60 + m

        times = [convert_to_minutes(timePoints[i]) for i in range(len(timePoints))]
        times.sort()

        min_difference = float('inf')
        for i in range(1, len(times)):
            min_difference = min(min_difference, times[i] - times[i - 1])

        midnight = 24 * 60
        return min(min_difference, midnight - times[-1] + times[0])



print(Solution().findMinDifference(["12:57","05:02","16:01"]))
