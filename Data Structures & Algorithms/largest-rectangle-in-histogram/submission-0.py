class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0
        for i in range(len(heights)):
            idx = i
            h = heights[i]
            while s and h<s[-1][1]:
                idx = s[-1][0]
                area = (i-idx) * s[-1][1]
                max_area = max(max_area, area)
                s.pop()
            s.append([idx, h])
            print(s, max_area)

        print("------")
        while s:
            idx = s[-1][0]
            h = s[-1][1]
            area = (len(heights)-idx)*h
            max_area = max(max_area, area)
            s.pop()
            print(s, area)
        
        return max_area