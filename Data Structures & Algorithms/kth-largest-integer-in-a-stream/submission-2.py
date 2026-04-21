class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for num in nums:
            heapq.heappush(self.h, -num)

    def add(self, val: int) -> int:
        q = deque()
        heapq.heappush(self.h, -val)
        for _ in range(self.k):
            q.append(heapq.heappop(self.h))
        
        ans = -q[-1]
        while q:
            heapq.heappush(self.h, q.popleft())
        
        return ans
