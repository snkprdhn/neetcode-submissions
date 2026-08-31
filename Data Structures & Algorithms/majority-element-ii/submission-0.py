class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = num2 = cnt1 = cnt2 = 0
        for num in nums:
            if num1 == num:
                cnt1 += 1
            elif num2 == num:
                cnt2 += 1
            elif not cnt1:
                num1 = num
                cnt1 = 1
            elif not cnt2:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        required_cnt = len(nums)//3
        cnt1 = cnt2 = 0
        for num in nums:
            if num==num1:
                cnt1 += 1
            elif num==num2:
                cnt2 += 1
        
        ans = []
        if cnt1>required_cnt:
            ans.append(num1)
        if cnt2>required_cnt:
            ans.append(num2)
        
        return ans