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

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.used = 0
        self.cache = {}
        self.stack = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.get(key) == -1:
            if self.used == self.capacity:
                del_key = self.stack.pop(0)
                del self.cache[del_key]
            else:
                self.used += 1

            self.cache[key] = value
            self.stack.append(key)
        else:
            self.cache[key] = value
