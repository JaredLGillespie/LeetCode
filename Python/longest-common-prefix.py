# https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        i = 0
        while True:
            char = None
            matched = True
            for str in strs:
                if i >= len(str):
                    matched = False
                    break
                if char is None:
                    char = str[i]
                    continue

                if str[i] != char:
                    matched = False
                    break

            if char is None or not matched:
                return ''.join(prefix)
            prefix.append(char)
            i += 1
