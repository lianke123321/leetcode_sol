# no Liana solution


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.iterators = [(len(v), iter(v)) for v in (v1, v2) if v]
        self.p = 0

    def next(self):
        """
        :rtype: int
        """
        length, iterator = self.iterators.pop(0)
        if length > 1:
            self.iterators.append((length - 1, iterator))
        return next(iterator)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.iterators) != 0

# Your ZigzagIterator object will be instantiated and called as such:
v1, v2 = [], []
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())
print v
