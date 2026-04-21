class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = prev * nums[i-1]
            prev = res[i]
        
        post = 1
        for i in range(len(nums)-2, -1, -1):
            post = nums[i+1] * post
            res[i] = res[i] * post
        
        return res
