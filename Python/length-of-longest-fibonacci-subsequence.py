# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/


class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def search_fibonacci(a, b):
            if (a + b) in subsequences:
                return subsequences[a, b]

            if a + b in numset:
                subsequences[a, b] = search_fibonacci(b, a + b) + 1
                return subsequences[a, b]

            return 0

        subsequences = {}
        numset = set(A)

        largest_subsequence = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if (A[i], A[j]) in subsequences: continue
                if (A[i] + A[j]) in numset:
                    largest_subsequence = max(largest_subsequence, search_fibonacci(A[i], A[j]) + 2)

        return largest_subsequence


print(Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
