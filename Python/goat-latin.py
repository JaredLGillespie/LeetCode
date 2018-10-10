# https://leetcode.com/problems/goat-latin


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        out = []
        for i, word in enumerate(S.split()):
            w = []
            if word[0].lower() in 'aeiou':
                w.append(word)
            else:
                w.append(word[1:])
                w.append(word[0])
            w.append('ma')
            w.extend(['a'] * (i + 1))
            out.append(''.join(w))

        return ' '.join(out)
