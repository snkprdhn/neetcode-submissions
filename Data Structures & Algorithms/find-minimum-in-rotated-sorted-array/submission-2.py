class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        min_num = float("infinity")

        while l<=r:
            mid = l + ((r-l)//2)
            num_mid = nums[mid]
            num_l = nums[l]
            num_r = nums[r]

            print(l, r, mid)
            min_num = min(min_num, num_mid)
            if num_mid < num_r:
                r = mid - 1
            else:
                l = mid + 1
        return min_num