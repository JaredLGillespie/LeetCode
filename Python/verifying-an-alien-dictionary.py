# https://leetcode.com/problems/verifying-an-alien-dictionary/


class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) < 2: return True
        order_index = {o: i for i, o in enumerate(order)}

        for i in range(0, len(words) - 1):
            prev_word, cur_word = words[i], words[i + 1]

            for j in range(min(len(prev_word), len(cur_word))):
                po, co = order_index[prev_word[j]], order_index[cur_word[j]]
                if po > co: return False
                if po < co: break
            else:
                if len(prev_word) > len(cur_word): return False

        return True
