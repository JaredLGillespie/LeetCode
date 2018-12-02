# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/


import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.contained_items = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        contained_element = False
        if val not in self.contained_items:
            contained_element = True
            self.contained_items[val] = set()

        self.contained_items[val].add(len(self.items))
        self.items.append(val)
        return contained_element

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.contained_items: return False
        index = self.contained_items[val].pop()
        if not self.contained_items[val]: del self.contained_items[val]

        if index != len(self.items) - 1:
            self.contained_items[self.items[-1]].remove(len(self.items) - 1)
            self.contained_items[self.items[-1]].add(index)
            self.items[index], self.items[-1] = self.items[-1], self.items[index]
        self.items.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.items[int(random.random() * len(self.items))]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


rc = RandomizedCollection()
rc.insert(1)
rc.insert(1)
rc.insert(2)
print(rc.getRandom())
rc.remove(1)
print(rc.getRandom())
print(rc.getRandom())
