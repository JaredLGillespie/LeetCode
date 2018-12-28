# https://leetcode.com/problems/letter-case-permutation/


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def helper(S, i):
            if i == len(S) - 1:
                if S[i].isalpha():
                    yield S[i].lower()
                    yield S[i].upper()
                else:
                    yield S[i]
            else:
                for x in helper(S, i + 1):
                    if S[i].isalpha():
                        yield S[i].lower() + x
                        yield S[i].upper() + x
                    else:
                        yield S[i] + x

        if not S: return [""]
        return list(helper(S, 0))
