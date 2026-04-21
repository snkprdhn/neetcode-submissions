class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        if nums[0]>0:
            return res

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1

            while j<k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum > 0:
                    k -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        
        return res
