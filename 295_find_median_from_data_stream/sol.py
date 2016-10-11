# no Liana solution
from heapq import heappop, heappush, heappushpop


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.small_heap, -heappushpop(self.large_heap, num))
        if len(self.large_heap) < len(self.small_heap):
            heappush(self.large_heap, -heappop(self.small_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.large_heap) > len(self.small_heap):
            return float(self.large_heap[0])
        return (self.large_heap[0] - self.small_heap[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.findMedian()
