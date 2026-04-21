"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key = lambda i:i.start)
        new_end = intervals[0].end

        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end

            if new_end > start:
                return False
            new_end = end
        
        return True