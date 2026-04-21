class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        new_start = intervals[0][0]
        new_end = intervals[0][1]
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if new_end < start:
                res.append([new_start, new_end])
                new_start, new_end = start, end
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        
        res.append([new_start, new_end])
        return res