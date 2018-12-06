# https://leetcode.com/problems/most-common-word/


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        freq = {}
        mfw = None
        mfc = 0
        for word in ''.join(w if w.isalpha() else ' ' for w in paragraph.lower()).split(' '):
            if not word or word in banned: continue
            if word not in freq: freq[word] = 0
            freq[word] += 1
            if freq[word] > mfc:
                mfc = freq[word]
                mfw = word
        return mfw


print(Solution().mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))
