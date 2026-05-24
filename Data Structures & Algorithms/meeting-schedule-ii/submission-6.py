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
        intervals.sort(key=lambda i: i.start) 
        d = dict()
        for interval in intervals:
            for i in range(interval.start, interval.end):
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        return max(d.values())