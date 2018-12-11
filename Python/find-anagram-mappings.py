# https://leetcode.com/problems/find-anagram-mappings/


class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        m = {}
        for i, b in enumerate(B):
            if b not in m: m[b] = i

        return [m[a] for a in A]
