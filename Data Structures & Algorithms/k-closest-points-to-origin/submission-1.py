class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = x**2 + y**2
            points[i] = (distance, points[i])
        
        k = k-1
        
        def quick_select(l, r):
            pivot, p = points[r][0], l
            for i in range(l, r):
                if points[i][0] < pivot:
                    points[i], points[p] = points[p], points[i]
                    p+=1
            
            points[p], points[r] = points[r], points[p]
            if p > k: return quick_select(l, p-1)
            elif p < k: return quick_select(p+1, r)
            else: return [point[1] for point in points[:p+1]]

        return quick_select(0, len(points)-1)


