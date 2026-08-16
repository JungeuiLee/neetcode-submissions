class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = [1] * n
        
        left = 0
        right = n - 1

        num = 1

        for i in range(n):
            lst[i] = num
            num *= nums[i]

        num2 = 1
        for i in range(n - 1, -1, -1):
            lst[i] *= num2
            num2 *= nums[i]

        return lst