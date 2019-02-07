# https://leetcode.com/problems/sum-of-even-numbers-after-queries/


class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even_sum = sum(x for x in A if x % 2 == 0)
        out = []

        for v, i in queries:
            if (A[i] % 2) == 0:
                if A[i] + v % 2 == 0:
                    even_sum += v
                else:
                    even_sum -= A[i]
            elif (A[i] + v % 2) == 0:
                even_sum += A[i] + v
            A[i] += v
            out.append(even_sum)
        return out
