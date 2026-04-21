"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_count = cur_count = 0
        heap = []

        for interval in intervals:
            heapq.heappush(heap, (interval.start, True))
            heapq.heappush(heap, (interval.end, False))
        
        while heap:
            time, is_start = heapq.heappop(heap)
            if is_start:
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                cur_count -= 1
        
        return max_count
