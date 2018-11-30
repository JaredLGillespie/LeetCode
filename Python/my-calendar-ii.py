# https://leetcode.com/problems/my-calendar-ii/


class MyCalendarTwo(object):

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for os, oe in self.overlaps:
            if os < end and start < oe: return False

        for bs, be in self.bookings:
            if bs < end and start < be:
                self.overlaps.append((max(bs, start), min(be, end)))

        self.bookings.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

cal = MyCalendarTwo()
for booking in [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]:
    print(cal.book(booking[0], booking[1]))
