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
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        # print(start, end)

        i = j = 0
        while i < len(start) and j < len(end):
            # print("start", i, j, cur_count)
            if start[i] >= end[j]:
                cur_count -= 1
                j+=1
            else:
                cur_count += 1
                i+=1
            # print("end", i, j, cur_count)
            max_count = max(max_count, cur_count)
        
        return max_count
