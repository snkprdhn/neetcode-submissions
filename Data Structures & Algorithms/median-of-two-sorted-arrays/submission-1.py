class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        l = 0
        r = m
        required_len = -(-(m + n) // 2) 

        while l <= r:
            mid = l + (r-l)//2
            
            l1 = l2 = float("-inf")
            r1 = r2 = float("inf")

            nums1_idx = mid
            nums2_idx = required_len - mid

            if nums1_idx > 0:
                l1 = nums1[nums1_idx-1]
            
            if nums2_idx > 0:
                l2 = nums2[nums2_idx-1]
            
            if nums1_idx < m:
                r1 = nums1[nums1_idx]
            
            if nums2_idx < n:
                r2 = nums2[nums2_idx]

            if l2 > r1:
                l = mid + 1
            elif l1 > r2:
                r = mid - 1
            else:
                if (m+n) % 2:
                    return max(l1, l2)
                
                return (max(l1, l2) + min(r1, r2)) / 2
            
        return 0
