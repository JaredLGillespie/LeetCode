# https://leetcode.com/problems/degree-of-an-array/


from collections import Counter


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        degree = max(freq.values())
        if degree <= 1: return degree

        degree_elements = {k: [-1, -1] for k in freq if freq[k] == degree}

        for i, n in enumerate(nums):
            if n in degree_elements:
                if degree_elements[n][0] == -1:
                    degree_elements[n][0] = i
                else:
                    degree_elements[n][1] = i

        min_length = float('inf')
        for de in degree_elements:
            min_length = min(min_length, degree_elements[de][1] - degree_elements[de][0] + 1)
        return min_length
