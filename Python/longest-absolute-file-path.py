# https://leetcode.com/problems/longest-absolute-file-path/


class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name: maxlen = max(maxlen, pathlen[depth] + len(name))
            else: pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen
