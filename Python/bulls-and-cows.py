# https://leetcode.com/problems/bulls-and-cows/


from collections import Counter


class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0, 0
        counter = Counter(list(secret))

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                counter[guess[i]] -= 1
                bulls += 1

        for i in range(len(guess)):
            if guess[i] == secret[i]: continue
            if guess[i] in counter and counter[guess[i]] > 0:
                cows += 1
                counter[guess[i]] -= 1

        return '%sA%sB' % (bulls, cows)
