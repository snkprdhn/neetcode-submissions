class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -(heapq.heappop(stones))
            y = -(heapq.heappop(stones))

            remain = x-y
            if remain:
                heapq.heappush(stones, -remain)
        
        if stones:
            return -(stones[0])
        return 0