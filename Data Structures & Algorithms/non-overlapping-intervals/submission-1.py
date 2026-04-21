class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])

        new_end = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if new_end > start:
                res += 1
                new_end = min(new_end, end)
            else:
                new_end = end
        
        return res