# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        smallest_group_size = float('inf')
        m = {}

        for card in deck:
            if card not in m:
                m[card] = 0
            m[card] += 1

        for card in m:
            smallest_group_size = min(smallest_group_size, m[card])

        if smallest_group_size < 2:
            return False

        for i in range(2, smallest_group_size + 1):
            for card in m:
                if m[card] % i != 0:
                    break
            else:
                return True

        return False
