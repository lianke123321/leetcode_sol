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

    def merge_self(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # some special cases
        if len(intervals) <= 1:
            return intervals

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            result = self.insert_self(result, intervals[i])

        return result

    def insert_self(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        new_interval_inserted = False

        if len(intervals) == 0:
            return [newInterval]

        while i < len(intervals):
            if start > intervals[i].end:
                result.append(intervals[i])
            elif end < intervals[i].start:
                if not new_interval_inserted:
                    result.append(Interval(start, end))
                    new_interval_inserted = True
                result.append(intervals[i])
            else:
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            i += 1

        if not new_interval_inserted:
            result.append(Interval(start, end))

        return result

sol = Solution()
test_intervals = [Interval(1, 4), Interval(1, 4)]
print sol.merge_self(test_intervals)
