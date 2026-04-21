class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = {}
        for src , dest, time in times:
            if src not in adj_map:
                adj_map[src] = []
            adj_map[src].append((time, dest))

        heap = [(0, k)]
        visited = set()
        max_time = 0

        while heap:
            t1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            
            max_time = max(max_time, t1)
            visited.add(n1)
            if n1 in adj_map:
                for t2, n2 in adj_map[n1]:
                    if n2 not in visited:
                        heapq.heappush(heap, (t1+t2, n2))
        
        return max_time if len(visited) == n else -1