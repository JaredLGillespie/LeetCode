# https://leetcode.com/problems/plus-one


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0:
                break
        else:
            digits.insert(0, 1)
        return digits
