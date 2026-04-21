class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]

        # Don't rob the last house
        prev_1 = prev_2 = 0
        for i in range(n-2, -1, -1):
            prev_1, prev_2 = max(prev_1, nums[i] + prev_2), prev_1
        ans_1 = prev_1

        # Don't rob the first house
        prev_1 = prev_2 = 0
        for i in range(n-1, 0, -1):
            prev_1, prev_2 = max(prev_1, nums[i] + prev_2), prev_1
        ans_2 = prev_1

        return max(ans_1, ans_2)