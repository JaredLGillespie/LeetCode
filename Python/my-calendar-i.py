# https://leetcode.com/problems/my-calendar-i/description/


class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, start, end):
        if not self.root:
            self.root = TreeNode(start, end)
            return True

        root = self.root
        while root:
            if root.start >= end:
                if not root.left:
                    root.left = TreeNode(start, end)
                    return True
                root = root.left
            elif root.end <= start:
                if not root.right:
                    root.right = TreeNode(start, end)
                    return True
                root = root.right
            else: return False
        return False


class MyCalendar(object):

    def __init__(self):
        self.bookings = Tree()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        return self.bookings.add(start, end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

