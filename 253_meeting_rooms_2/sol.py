# no Liana solution


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])

        p1, p2, rooms_used, available = 0, 0, 0, 0
        while p1 < len(starts):
            if starts[p1] < ends[p2]:
                if available == 0:
                    rooms_used += 1
                else:
                    available -= 1
                p1 += 1
            else:
                available += 1
                p2 += 1
        return rooms_used
