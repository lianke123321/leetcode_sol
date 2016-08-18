# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'

    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'


class Solution:
    def merge(self, intervals):
        if len(intervals)<2:
            return intervals

        result=[]
        result.append(intervals[0])

        for i in range(1,len(intervals)):
            result=self.insert(result,intervals[i])

        return result

    def insert(self,intervals,newInterval):
        result=[]
        for interval in intervals:
        #case 1   (...) {...}   or {...} (...)
            if interval.start > newInterval.end or interval.end < newInterval.start :
                result.append(interval)
                continue
        #case 2    ( ...{ ... } ...)
            elif interval.start <= newInterval.start and interval.end >=newInterval.end :
                return intervals
        #case 3   (..{...)...}   {...(...}...)   {...(...)...}
            else:
                newInterval.end=max(newInterval.end,interval.end)
                newInterval.start=min(newInterval.start,interval.start)
        result.append(newInterval)
        return result


class Solution_self:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for i in sorted(intervals, key=lambda i: i.start):
            if result and i.start <= result[-1].end:
                result[-1].end = max(result[-1].end, i.end)
            else:
                result.append(i)
        return result

sol = Solution_self()
test_intervals = [Interval(1, 4), Interval(1, 4)]
print sol.merge(test_intervals)
