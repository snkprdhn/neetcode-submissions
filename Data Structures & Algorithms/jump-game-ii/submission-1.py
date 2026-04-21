class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_jump = 0
        cur_jump_end = 0
        jumps = 0
        
        for i in range(n-1):
            max_jump = max(max_jump, i + nums[i])

            if i == cur_jump_end:
                jumps += 1
                cur_jump_end = max_jump
            
        return jumps