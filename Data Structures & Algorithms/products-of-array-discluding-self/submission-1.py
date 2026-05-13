class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        cur = 1

        for i in range(len(nums)):
            prefixProduct[i] *= cur
            cur = cur * nums[i]
        
        cur = 1

        for i in range(len(nums)-1, -1, -1):
            prefixProduct[i] *= cur
            cur = cur * nums[i]
        
        return prefixProduct