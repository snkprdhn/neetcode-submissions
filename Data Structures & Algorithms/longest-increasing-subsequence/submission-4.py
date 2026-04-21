class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        n = len(nums)

        def b_search(tail, num):
            l = 0
            h = len(tail)-1
            while l<=h:
                mid = l + (h-l) // 2
                if tail[mid] < num:
                    l = mid + 1
                else:
                    h = mid - 1        
            return l

        for n in nums:
            i = b_search(tail, n)
            if i == len(tail):
                tail.append(n)
            else:
                tail[i] = n
        
        return len(tail)