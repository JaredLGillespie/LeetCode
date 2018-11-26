# https://leetcode.com/problems/fizz-buzz/


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def f(x):
            if x % 3 == x % 5 == 0:
                return 'FizzBuzz'
            elif x % 3 == 0:
                return 'Fizz'
            elif x % 5 == 0:
                return 'Buzz'
            return str(x)

        return list(map(f, range(1, n + 1)))
