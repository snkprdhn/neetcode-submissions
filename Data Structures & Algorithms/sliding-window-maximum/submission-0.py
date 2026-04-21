class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=r=0
        q = collections.deque()
        res = []

        while r<len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if r-l+1 == k:
                res.append(nums[q[0]])
                l+=1
                if q[0] < l:
                    q.popleft()
            r+=1

        return res