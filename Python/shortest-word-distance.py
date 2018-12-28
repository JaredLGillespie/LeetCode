# https://leetcode.com/problems/shortest-word-distance/


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cur_word, cur_pos, shortest_dist = None, -1, float('inf')

        for i, word in enumerate(words):
            if word in (word1, word2):
                if cur_word is None:
                    cur_word = word
                    cur_pos = i
                else:
                    if cur_word != word:
                        shortest_dist = min(shortest_dist, i - cur_pos)
                        cur_word = word
                        cur_pos = i
                    else:
                        cur_pos = i

        return shortest_dist
