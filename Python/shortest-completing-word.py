# https://leetcode.com/problems/shortest-completing-word/


from collections import Counter


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lp = Counter([c for c in licensePlate.lower() if c.isalpha()])
        smallest_word = None

        for word in words:
            if smallest_word is None or len(smallest_word) > len(word):
                wc = Counter(word.lower())
                for c in lp:
                    if wc[c] < lp[c]:
                        break
                else:
                    smallest_word = word

        return smallest_word
