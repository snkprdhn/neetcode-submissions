class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = Counter(nums)
        max_len = 0
        for num in nums:
            cur_len = 1
            while num-1 in num_map:
                cur_len += 1
                num -= 1
            max_len = max(max_len, cur_len)
            
        print(num_map)
        return max_len