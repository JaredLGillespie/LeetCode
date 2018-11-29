# https://leetcode.com/problems/word-break-ii/


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def search(index):
            if index == len(s): return [[]]
            if index in memo: return memo[index]

            sentences_made = []
            for word in wordDict:
                if len(word) > len(s) - index: continue
                if s[index:index + len(word)] == word:
                    sm = search(index + len(word))
                    for r in sm: sentences_made.append([word] + r)

            memo[index] = sentences_made
            return sentences_made

        memo = {}
        return list(map(lambda x: ' '.join(x), search(0)))
