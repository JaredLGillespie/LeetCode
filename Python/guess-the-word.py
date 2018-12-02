# https://leetcode.com/problems/guess-the-word/


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def filter_wordset(matches, word, wordset):
            new_wordset = set()
            for other in wordset:
                similar_chars = 0
                for i in range(6):
                    if other[i] == word[i]: similar_chars += 1
                    if similar_chars > matches: break
                if similar_chars == matches:
                    new_wordset.add(other)
            return new_wordset

        wordset = set(wordlist)
        word = wordset.pop()
        guess = master.guess(word)

        while guess != 6:
            wordset = filter_wordset(guess, word, wordset)
            word = wordset.pop()
            guess = master.guess(word)
