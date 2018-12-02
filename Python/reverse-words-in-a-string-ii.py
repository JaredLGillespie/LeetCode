# https://leetcode.com/problems/reverse-words-in-a-string-ii/


class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(l, r):
            while l < r:
                str[l], str[r] = str[r], str[l]
                l += 1
                r -= 1

        reverse(0, len(str) - 1)

        l, r = 0, 0
        while r < len(str):
            while r < len(str) and str[r] != ' ':
                r += 1
            reverse(l, r - 1)
            r += 1
            l = r

        reverse(l, r)
