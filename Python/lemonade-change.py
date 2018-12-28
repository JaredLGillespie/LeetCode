# https://leetcode.com/problems/lemonade-change/


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0: return False
                fives -= 1
                tens += 1
            else:
                if fives == 0 or tens == 0: return False
                fives -= 1
                tens -= 1
        return True
