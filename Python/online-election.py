# https://leetcode.com/problems/online-election

class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.leaders = self._process_votes(persons)

    def _process_votes(self, persons):
        leaders = [0] * len(persons)
        freq = {}
        winning_person = 0
        highest_count = 0
        for i, person in enumerate(persons):
            if person not in freq:
                freq[person] = 0
            freq[person] += 1

            if freq[person] >= highest_count:
                highest_count = freq[person]
                winning_person = person
            leaders[i] = winning_person
        return leaders


    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t >= self.times[-1]:
            return self.leaders[-1]

        l, r = 0, len(self.times)

        while l <= r:
            m = (l + r) // 2
            if self.times[m] == t:
                return self.leaders[m]
            elif self.times[m] < t:
                l = m + 1
            else:
                r = m - 1

        return self.leaders[r]
