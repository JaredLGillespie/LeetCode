# https://leetcode.com/problems/find-common-characters/


from collections import Counter
from string import ascii_lowercase


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        counters = [Counter(a) for a in A]

        ret = []
        for c in ascii_lowercase:
            m = min(count[c] for count in counters)
            for i in range(m):
                ret.append(c)

        return ret
