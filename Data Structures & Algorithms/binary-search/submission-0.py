class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            idx = l + ((r-l)//2)
            if nums[idx]<target:
                l = idx+1
            elif nums[idx]>target:
                r = idx-1
            else:
                return idx
        return -1