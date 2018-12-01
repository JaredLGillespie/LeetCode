# https://leetcode.com/problems/k-similar-strings/


from collections import deque


class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]: break

            T = list(S)
            for j in range(i + 1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield ''.join(T)
                    T[i], T[j] = T[j], T[i]

        queue = deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)
