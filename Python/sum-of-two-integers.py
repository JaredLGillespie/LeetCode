class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX, MASK = 0x7FFFFFFF, 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return a if a <= MAX else ~(a ^ MASK)
