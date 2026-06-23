class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            num = nums[i]
            if 0<num<=n and num!=(i+1) and nums[num-1]!=num:
                nums[i], nums[num-1] = nums[num-1], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1
