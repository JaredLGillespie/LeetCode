# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        return sum(s in J for s in S)
