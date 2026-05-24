"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0 
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        s = 0
        e = 0
        res = 1
        count = 1
        while e < (len(end)) and s < (len(start)):
            if start[s] < end[e]:
                res = max(res, count)
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
        return res