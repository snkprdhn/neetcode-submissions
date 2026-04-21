class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        l,r = 0, len(height)-1
        total = 0
        max_l, max_r = height[0], height[-1]

        while l<r:
            if max_l<=max_r:
                l+=1
                max_l = max(max_l, height[l])
                cur = max_l - height[l]
            else:
                r-=1
                max_r = max(max_r, height[r])
                cur = max_r - height[r]

            if cur>0:
                total += cur
            print(l, r, max_l, max_r, cur, total)


        return total