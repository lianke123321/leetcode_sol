# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'

    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1
        result.append(Interval(start, end))
        result += intervals[i:]
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
test_intervals = [Interval(1, 5)]
new_interval = Interval(2, 3)
print sol.insert_self(test_intervals, new_interval)
