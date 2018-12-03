# https://leetcode.com/problems/unique-word-abbreviation/


class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbrevs = {}
        for word in dictionary:
            if len(word) == 0: continue
            abbrev = word[0] + str(len(word) - 2) + word[-1]
            if abbrev not in self.abbrevs: self.abbrevs[abbrev] = set()
            self.abbrevs[abbrev].add(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == '': return True
        abbrev = word[0] + str(len(word) - 2) + word[-1]
        if abbrev not in self.abbrevs: return True
        if len(self.abbrevs[abbrev]) > 1: return False
        if word not in self.abbrevs[abbrev]: return False
        return True


vwa = ValidWordAbbr(['hello'])
print(vwa.isUnique('hello'))

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
