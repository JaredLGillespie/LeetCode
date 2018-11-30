# https://leetcode.com/problems/maximum-product-of-word-lengths/


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = {}
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            if mask not in masks: masks[mask] = len(word)
            else: masks[mask] = max(masks[mask], len(word))

        max_product = 0
        for m1 in masks:
            for m2 in masks:
                if m1 & m2: continue
                max_product = max(max_product, masks[m1] * masks[m2])
        return max_product


print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
