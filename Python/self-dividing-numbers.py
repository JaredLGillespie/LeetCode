# https://leetcode.com/problems/self-dividing-numbers/


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sdn = []
        for i in range(left, right + 1):
            for d in map(int, str(i)):
                if d == 0: break
                if i % d != 0: break
            else: sdn.append(i)
        return sdn
