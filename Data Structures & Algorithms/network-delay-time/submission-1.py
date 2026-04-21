class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = {}
        for src , dest, time in times:
            if src not in adj_map:
                adj_map[src] = []
            adj_map[src].append((dest, time))
        
        if len(times) < n-1:
            return -1
        
        time_map = {node: float("inf") for node in range(1, n+1)}

        def dfs(node, time):
            if time >= time_map[node]:
                return

            time_map[node] = time
            if node in adj_map:
                for edge, w in adj_map[node]:
                    dfs(edge, time+w)        
        
        dfs(k, 0)
        res = max(time_map.values())
        return res if res < float("inf") else -1