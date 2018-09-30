# https://leetcode.com/problems/word-subsets


class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        A_FREQ_MAP = self.create_freq_map(A)
        B_MAX_FREQ_MAP = self.create_max_freq_map(B)

        valid = []
        for a in A:
            if self.is_subset(A_FREQ_MAP[a], B_MAX_FREQ_MAP):
                valid.append(a)

        return valid

    def create_freq_map(self, X):
        MAP = {}
        for x in X:
            m = {}

            for c in x:
                if c not in m:
                    m[c] = 0
                m[c] += 1

            MAP[x] = m
        return MAP

    def create_max_freq_map(self, X):
        MAX_FREQ_MAP = {}
        FREQ_MAP = self.create_freq_map(X)

        for x in FREQ_MAP:
            for k, v in FREQ_MAP[x].items():
                if k not in MAX_FREQ_MAP:
                    MAX_FREQ_MAP[k] = v
                else:
                    MAX_FREQ_MAP[k] = max(MAX_FREQ_MAP[k], v)
        return MAX_FREQ_MAP

    def is_subset(self, a_freq_map, b_freq_map):
        for c in b_freq_map:
            if c not in a_freq_map or b_freq_map[c] > a_freq_map[c]:
                return False
        return True
