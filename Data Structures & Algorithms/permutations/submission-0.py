class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(idx):
            if idx == n:
                res.append(nums[:])

            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]
        
        backtrack(0)
    
        return res

            
            