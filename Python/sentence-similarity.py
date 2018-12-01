# https://leetcode.com/problems/sentence-similarity/


class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        similar_words = {}
        for a, b in pairs:
            if a not in similar_words: similar_words[a] = set()
            if b not in similar_words: similar_words[b] = set()
            similar_words[a].add(b)
            similar_words[b].add(a)

        for i in range(len(words1)):
            a, b = words1[i], words2[i]
            if a == b: continue
            if a in similar_words and b in similar_words[a]: continue
            return False
        return True
