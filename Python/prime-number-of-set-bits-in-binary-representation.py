# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        return sum(bin(x).count('1') in primes for x in range(L, R + 1))

