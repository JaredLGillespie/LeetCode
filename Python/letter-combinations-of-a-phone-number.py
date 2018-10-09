# https://leetcode.com/problems/letter-combinations-of-a-phone-number


m = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        s = []
        for d in digits:
            if not s:
                s = [c for c in m[d]]
            else:
                sn = []
                for c in m[d]:
                    sc = [x + c for x in s]
                    sn.extend(sc)
                s = sn
        return s
