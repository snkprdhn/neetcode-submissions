class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]

        def rob(num_list):
            n = len(num_list)
            prev_1 = prev_2 = 0
            for i in range(n-1, -1, -1):
                prev_1, prev_2 = max(prev_1, num_list[i] + prev_2), prev_1
            return prev_1

        return max(
            rob(nums[:n-1]), # Don't rob the last house
            rob(nums[1:]) # Don't rob the first house
        )