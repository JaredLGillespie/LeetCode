
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1 / x

        r = 1
        while n:
            if n % 2 == 1:
                r *= x
            n //= 2
            x *= x
        return r
