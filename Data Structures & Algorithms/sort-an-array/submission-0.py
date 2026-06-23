class Solution:
    def merge(self, nums, left, right):
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            nums[k] = left[i]
            i+=1
            k+=1

        while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n > 1:
            left = self.sortArray(nums[:n//2])
            right = self.sortArray(nums[n//2:])
            self.merge(nums, left, right)
        return nums
