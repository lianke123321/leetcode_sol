# no Liana solution


from collections import deque


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque()
        self.count = 0
        self.average = 0
        self.sz = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        if self.count < self.sz:
            self.average = float(val) if not self.count \
                else (self.average * self.count + val) / (self.count + 1)
            self.count += 1
        else:
            self.average += float(val - self.q.popleft()) / self.sz
        return self.average

m = MovingAverage(3)
print m.next(1)
print m.next(10)
print m.next(3)
print m.next(5)
