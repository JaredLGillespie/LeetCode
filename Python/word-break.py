# https://leetcode.com/problems/word-break/


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def search(index):
            if index == len(s): return True
            if index in memo: return False

            for word in wordDict:
                if len(word) > len(s) - index: continue

                for i in range(len(word)):
                    if s[index + i] != word[i]: break
                else:
                    if search(index + len(word)): return True
            memo.add(index)
            return False

        memo = set()
        return search(0)
