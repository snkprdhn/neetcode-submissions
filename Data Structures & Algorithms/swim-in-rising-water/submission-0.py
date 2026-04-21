class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        max_time = float("-inf")
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        while heap:
            time, i, j = heapq.heappop(heap)
            max_time = max(max_time, time)
            if i == len(grid)-1 and j == len(grid[0])-1:
                return max_time

            visited.add((i, j))
            for r, c in dirs:
                new_r = i+r
                new_c = j+c
                if (new_r, new_c) in visited or new_r < 0 or new_c < 0 or new_r == len(grid) or new_c == len(grid[0]):
                    continue
                
                heapq.heappush(heap, (grid[new_r][new_c], new_r, new_c))
                
