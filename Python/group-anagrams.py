# https://leetcode.com/problems/group-anagrams


class Solution:
    def groupAnagrams(self, strs):
        m = {}
        for str in strs:
            s = ''.join(sorted(str))
            if s not in m:
                m[s] = []
            m[s].append(str)

        return [i for i in m.values()]
