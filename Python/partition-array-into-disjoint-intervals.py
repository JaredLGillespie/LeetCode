# https://leetcode.com/problems/partition-array-into-disjoint-intervals


class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        largest_in_partition = A[0]
        largest_seen = A[0]
        pp = 0

        for i in range(1, len(A)):
            if A[i] < largest_in_partition:
                pp = i
                largest_in_partition = largest_seen
            else:
                largest_seen = max(largest_seen, A[i])
        return pp + 1
