class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        new_start = newInterval[0]
        new_end = newInterval[1]

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if new_end < start:
                res.append([new_start, new_end])
                return res + intervals[i:]
            elif new_start > end:
                res.append(intervals[i])
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        
        res.append([new_start, new_end])
        return res
                