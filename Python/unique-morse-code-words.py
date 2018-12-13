# https://leetcode.com/problems/unique-morse-code-words/


mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformations = set()
        for word in words:
            transformations.add(''.join([mapping[ord(c) - ord('a')] for c in word]))
        return len(transformations)
