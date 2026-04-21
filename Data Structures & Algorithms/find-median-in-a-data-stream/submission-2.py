class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, -(num))

        if (self.min_heap and self.max_heap) and (-(self.min_heap[0]) > self.max_heap[0]):
            heapq.heappush(self.max_heap, -(heapq.heappop(self.min_heap)))
        
        if len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -(heapq.heappop(self.min_heap)))
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -(heapq.heappop(self.max_heap)))

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return -(self.min_heap[0])
        elif len(self.max_heap) > len(self.min_heap) :
                return self.max_heap[0]
        else:
            a = b = 0
            if self.min_heap:
                a = -(self.min_heap[0])
            if self.max_heap:
                b = self.max_heap[0]
            return (a+b)/2
        