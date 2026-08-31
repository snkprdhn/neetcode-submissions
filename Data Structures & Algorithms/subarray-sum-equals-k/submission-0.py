class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_map = defaultdict(int)
        prefix = []
        prev = 0
        sum_cnt = 0
        for num in nums:
            prefix_map[prev] += 1
            prev += num
            remaining = prev - k
            sum_cnt += prefix_map[remaining]
        return sum_cnt

