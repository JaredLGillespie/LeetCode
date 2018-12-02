# https://leetcode.com/problems/find-and-replace-in-string/


class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        def source_match(index, source):
            if index + len(source) > len(S): return False
            return S[index:index + len(source)] == source

        out = list(S)
        for index, source, target in zip(indexes, sources, targets):
            if source_match(index, source):
                out[index] = target
                for i in range(index + 1, index + len(source)):
                    out[i] = ''

        return ''.join(out)
