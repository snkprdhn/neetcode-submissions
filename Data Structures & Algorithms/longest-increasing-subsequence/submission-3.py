import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        n = len(nums)
        for n in nums:
            i = bisect.bisect_left(tail, n)
            if i == len(tail):
                tail.append(n)
            else:
                tail[i] = n
        
        return len(tail)