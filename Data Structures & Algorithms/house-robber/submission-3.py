class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev_1 = prev_2 = 0

        for i in range(n-1, -1, -1):
            prev_1, prev_2 = max(prev_1, nums[i] + prev_2), prev_1
        
        return prev_1