class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        req_sum = n * (n+1)//2
        cur_sum = sum(nums)

        return 0 if req_sum == cur_sum else req_sum-cur_sum