# https://leetcode.com/problems/count-primes/


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        m = int(pow(n, 0.5)) + 1
        for i in range(2, m):
            if not primes[i]: continue
            for j in range(2, (n - 1) // i + 1):
                primes[i * j] = False
        return sum(primes)


print(Solution().countPrimes(999983))
