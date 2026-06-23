class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = k = 0
        n = len(nums)
        for j in range(n):
            if nums[j]!=val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                k += 1
        
        return k