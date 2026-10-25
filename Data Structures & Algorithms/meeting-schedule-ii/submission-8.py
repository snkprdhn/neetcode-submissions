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
        
        intervals.sort(key = lambda x:x.start)
        rooms = []
        heapq.heappush(rooms, intervals[0].end)
        max_rooms = 1
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            while rooms and start >= rooms[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, end)
            max_rooms = max(max_rooms, len(rooms))
        
        return max_rooms