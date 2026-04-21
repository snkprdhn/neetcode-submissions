class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep multiplying untill you reach a 0 or -ve product, 
        # set to the next element and start again

        min_product = max_product = res = nums[0]
        for n in nums[1:]:
            temp = max_product
            max_product = max(n, max_product * n, min_product * n)
            min_product = min(n, temp * n, min_product * n)
            res = max(res, max_product)
        
        return res

            