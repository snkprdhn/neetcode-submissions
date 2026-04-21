class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = (x**2 + y**2)**0.5
            points[i] = (-distance, points[i])

        print(points)
        heapq.heapify(points)
        while len(points) > k:
            heapq.heappop(points)
        
        return [p[1] for p in points]

