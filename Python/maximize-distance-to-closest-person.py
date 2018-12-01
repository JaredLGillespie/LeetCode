# https://leetcode.com/problems/maximize-distance-to-closest-person/


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        distance_to_left = [0] * len(seats)
        distance_to_right = [0] * len(seats)
        dist = 0
        seat_seen = False
        for i in range(len(seats)):
            if seats[i] == 1:
                distance_to_left[i] = float('inf')
                seat_seen = True
                dist = 0
            else:
                if seat_seen: distance_to_left[i] = dist
                else: distance_to_left[i] = float('inf')
                dist += 1

        seat_seen = False
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                distance_to_right[i] = float('inf')
                seat_seen = True
                dist = 0
            else:
                if seat_seen: distance_to_right[i] = dist
                else: distance_to_right[i] = float('inf')
                dist += 1

        max_distance = 0
        for i in range(len(seats)):
            if seats[i] == 1: continue
            max_distance = max(max_distance, min(distance_to_right[i], distance_to_left[i]))

        return max_distance + 1 if max_distance != float('inf') else 1
