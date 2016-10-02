# class LRUCache(object):
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.used = 0
#         self.cache = {}
#         self.stack = []
#
#     def get(self, key):
#         """
#         :rtype: int
#         """
#         if self.cache.has_key(key):
#             self.stack.remove(key)
#             self.stack.append(key)
#             return self.cache[key]
#         else:
#             return - 1
#
#     def set(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: nothing
#         """
#         if self.get(key) == - 1:
#             if self.used == self.capacity:
#                 delkey = self.stack.pop(0)
#                 del self.cache[delkey]
#                 self.cache[key] = value
#                 self.stack.append(key)
#             else:
#                 self.cache[key] = value
#                 self.stack.append(key)
#                 self.used += 1
#         else:
#             self.cache[key] = value  # update the value of the key

from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.cache:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.cache.popitem(last=False)
        else:
            self.cache.pop(key)
        self.cache[key] = value

lru = LRUCache(2)
lru.set(2, 1)
lru.set(1, 1)
lru.set(2, 3)
lru.set(4, 1)
print lru.get(1)
print lru.get(2)
