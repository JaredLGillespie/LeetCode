# https://leetcode.com/problems/design-hashmap/


class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root is None:
            self.root = LinkedListNode(key, value)
        else:
            node = self.root
            while node.next and node.key != key:
                node = node.next

            if node.key == key:
                node.value = value
            else:
                node.next = LinkedListNode(key, value)

    def get(self, key):
        if not self.root: return -1
        node = self.root
        while node.next and node.key != key:
            node = node.next

        if node.key == key:
            return node.value
        return -1

    def remove(self, key):
        if not self.root: return
        node, prev = self.root, None
        while node.next and node.key != key:
            prev = node
            node = node.next

        if node.key == key:
            if prev: prev.next = node.next
            else: self.root = node.next


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [LinkedList() for _ in range(1000)]

    def hash_func(self, key):
        return key % len(self.table)

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = self.hash_func(key)
        self.table[index].put(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self.hash_func(key)
        return self.table[index].get(key)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = self.hash_func(key)
        self.table[index].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


hm = MyHashMap()
hm.put(1, 1)
hm.put(2, 2)
hm.get(1)
hm.get(3)
hm.put(2, 1)
hm.get(2)
hm.remove(2)
hm.get(2)
