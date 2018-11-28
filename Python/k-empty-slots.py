# https://leetcode.com/problems/k-empty-slots/


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * len(flowers)
        for i in range(len(flowers)):
            days[flowers[i] - 1] = i + 1

        i, l, r = 0, 0, k + 1
        res = float('inf')
        while r < len(days):
            di, dl, dr = days[i], days[l], days[r]
            if days[i] < days[l] or days[i] <= days[r]:
                if i == r: res = min(res, max(days[l], days[r]))
                l = i
                r = i + k + 1
            i += 1

        return res if res != float('inf') else -1
