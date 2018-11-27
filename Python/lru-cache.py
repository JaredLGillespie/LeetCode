# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def append(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self.size += 1

    def remove(self, node):
        if self.head == node:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

        if self.tail == node:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next

        node.next = None
        node.prev = None
        self.size -= 1

    def pop(self):
        if not self.tail:
            return None

        tail = self.tail
        if self.tail.prev:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.head = None
            self.tail = None

        tail.prev = None
        self.size -= 1
        return tail


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.cache = LinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            node = self.map[key]
            self.cache.remove(node)
            self.cache.append(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.map:
            if len(self.cache) == self.capacity:
                node = self.cache.pop()
                del self.map[node.key]

            node = Node(key, value)
            self.cache.append(node)
            self.map[key] = node
        else:
            node = self.map[key]
            self.cache.remove(node)
            self.cache.append(node)
            node.value = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))
cache.put(1, 1)
cache.put(4, 1)
print(cache.get(2))
