# https://leetcode.com/contest/problems/max-consecutive-ones-iii/


from collections import deque


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        C = [0] * len(A)
        for i in range(len(A) - 1):
            if A[i] == 1:
                C[i + 1] = C[i] + A[i]

        longest = 0
        curlength = 0
        k = 0
        placed = deque()
        for i in range(len(A)):
            if A[i] == 0:
                if K == 0:
                    curlength = 0
                elif k < K:
                    curlength += 1
                    k += 1
                    placed.append(i)
                    longest = max(curlength, longest)
                else:
                    curlength -= C[placed.popleft()]
                    placed.append(i)
                    longest = max(curlength, longest)
            else:
                curlength += 1
                longest = max(curlength, longest)

        return longest
